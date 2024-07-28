from pynput import keyboard
import requests
import time

# Api for getting random words
word_site = "https://random-word-api.vercel.app/api?words=1"

# Request and response handling for word
response = requests.get(word_site)
word = response.content.decode('utf-8').replace('[', '').replace(']', '').replace('"', '')

validInputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Hangman Visuals
hangman_stages = {
	1: """
       __________________________
      /                          |
      |                          |
      |                          |
      |                       
      |                      
      |                       
      |                       
      |                          
      |                          
      |                          
      |                           
      |                            
      |                             
      |                          
      |                          
      |                           
      |                            
      |                            
      |                              
      |                               
______|______
""",
	2: """
       __________________________
      /                          |
      |                          |
      |                        __|__
      |                       /     \\
      |                       | | | |
      |                       |  o  |
      |                       \_____/
      |                          
      |                          
      |                          
      |                           
      |                            
      |                             
      |                          
      |                          
      |                           
      |                            
      |                            
      |                              
      |                               
______|______
""",
	3: """
       __________________________
      /                          |
      |                          |
      |                        __|__
      |                       /     \\
      |                       | | | |
      |                       |  o  |
      |                       \_____/
      |                          |
      |                          |
      |                          |
      |                          | 
      |                          |  
      |                          |   
      |                          |
      |                          
      |                           
      |                            
      |                            
      |                              
      |                               
______|______
""",
	4: """
       __________________________
      /                          |
      |                          |
      |                        __|__
      |                       /     \\
      |                       | | | |
      |                       |  o  |
      |                       \_____/
      |                          |
      |                          |
      |                         /|
      |                        / | 
      |                       /  |  
      |                      /   |   
      |                          |
      |                          
      |                           
      |                            
      |                            
      |                              
      |                               
______|______
""",
	5: """
       __________________________
      /                          |
      |                          |
      |                        __|__
      |                       /     \\
      |                       | | | |
      |                       |  o  |
      |                       \_____/
      |                          |
      |                          |
      |                         /|\\
      |                        / | \\
      |                       /  |  \\
      |                      /   |   \\
      |                          |
      |                          
      |                           
      |                            
      |                            
      |                              
      |                               
______|______
""",
	6: """
       __________________________
      /                          |
      |                          |
      |                        __|__
      |                       /     \\
      |                       | | | |
      |                       |  o  |
      |                       \_____/
      |                          |
      |                          |
      |                         /|\\
      |                        / | \\
      |                       /  |  \\
      |                      /   |   \\
      |                          |
      |                         / 
      |                        /   
      |                       /     
      |                      /       
      |                     /         
      |                    /           
______|______
""",
	7: """
       __________________________
      /                          |
      |                          |
      |                        __|__
      |                       /     \\
      |                       | | | |
      |                       |  o  |
      |                       \_____/
      |                          |
      |                          |
      |                         /|\\
      |                        / | \\
      |                       /  |  \\
      |                      /   |   \\
      |                          |
      |                         / \\
      |                        /   \\
      |                       /     \\
      |                      /       \\
      |                     /         \\
      |                    /           \\
______|______
"""
}

# State for program
correct_letters = []
incorrect_letters = []
started = False


def get_letters_in_word():
	guess = ""

	# If the letter in the word is in guessed, put the letter in guess string
	# Otherwise, put a "_"
	for char in word:
			if char in correct_letters:
				guess += f" {char} "
			else:
				guess += " _ "

	return guess


# Starting print
print("""  _____                                         _               
 |  __ \                                       | |              
 | |__) | __ ___  ___ ___    __ _ _ __  _   _  | | _____ _   _  
 |  ___/ '__/ _ \/ __/ __|  / _` | '_ \| | | | | |/ / _ \ | | | 
 | |   | | |  __/\__ \__ \ | (_| | | | | |_| | |   <  __/ |_| | 
 |_|   |_|  \___||___/___/  \__,_|_| |_|\__, | |_|\_\___|\__, | 
                                         __/ |            __/ | 
               _              _         |___/   _        |___/  
              | |            | |           | | | |              
              | |_ ___    ___| |_ __ _ _ __| |_| |              
              | __/ _ \  / __| __/ _` | '__| __| |              
              | || (_) | \__ \ || (_| | |  | |_|_|              
               \__\___/  |___/\__\__,_|_|   \__(_)              
                                                                
                                                                """)


# Main function
def on_press(key):
	try:
		k = key.char.lower()  # single-char keys
	except:
		k = key.name  # other keys

	global started

	if key == keyboard.Key.esc: # Program exits if Escape key is pressed
		return False
	elif not started: # Runs only once, at the start of the game
		started = True

		print(hangman_stages[1])

		guessing = get_letters_in_word()
		print(guessing)
	elif k in validInputs:
		if k in correct_letters or k in incorrect_letters: # Prevent duplicate guesses
			print("Please type a letter you have not guessed yet")
		else:
			count = word.count(k) # Count how many of the guessed letter is in the word

			# Add letter to correct list if at least 1 appears in the word, else add letter to incorrect list
			if count > 0:
				correct_letters.append(k)
			else:
				incorrect_letters.append(k)

			print(hangman_stages[len(incorrect_letters)+1])

			print(f"Wrong letters: {' '.join(incorrect_letters).upper()}") # Convert list of incorrect letters into a printable string
			if count == 1:
				print(f"The word has {count} {k}")
			else:
				print(f"The word has {count} {k}'s")

			guessing = get_letters_in_word()
			print(guessing)

			# Convert the string printed to a word that can be checked
			# Ex. turns h _ l l _ into h_ll_ or w o r d into word
			check = guessing.replace(" ", "")

			if check == word:
				# Win print
				print(""" __     __          __          __         _ 
 \ \   / /          \ \        / /        | |
  \ \_/ /__  _   _   \ \  /\  / /__  _ __ | |
   \   / _ \| | | |   \ \/  \/ / _ \| '_ \| |
    | | (_) | |_| |    \  /\  / (_) | | | |_|
    |_|\___/ \__,_|     \/  \/ \___/|_| |_(_)
                                             
                                             """)
				
				# Wait for 5 seconds before program exit
				time.sleep(5)

				return False

			if len(incorrect_letters) == 6: # If amount of incorrect guesses equals 6 aka hangman is fully formed then player loses
				# Lose print
				print(""" __     __           _               _   _ 
 \ \   / /          | |             | | | |
  \ \_/ /__  _   _  | |     ___  ___| |_| |
   \   / _ \| | | | | |    / _ \/ __| __| |
    | | (_) | |_| | | |___| (_) \__ \ |_|_|
    |_|\___/ \__,_| |______\___/|___/\__(_)
                                           
                                           """)
				print(f"The word was: {word}")
				
				# Wait for 5 seconds before program exit
				time.sleep(5)


				return False
	else:
		print("Please type a valid character")

listener = keyboard.Listener(on_press=on_press) # bind main function (on_press) to a keyboard listener; runs every keyboard input
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys