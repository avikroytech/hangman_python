from tkinter import *
from tkinter import ttk
from tkinter import font
import requests

# Api for getting random words
word_site = "https://random-word-api.vercel.app/api?words=1"

# Request and response handling for word
response = requests.get(word_site)
word = response.content.decode('utf-8').replace('[', '').replace(']', '').replace('"', '')

# word = "hangman"


# State for program
correct_letters = []
incorrect_letters = []

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

def disable_all_guess_buttons():
	buttons = button_frame.winfo_children() # Get buttons

	for button in buttons: # Iterate through all buttons and disable them if not already
		if button.instate(['!disabled']):
			button.state(['disabled'])

def enable_all_guess_buttons():
	buttons = button_frame.winfo_children() # Get buttons

	for button in buttons: # Iterate through all buttons and enable them if not already
		if button.instate(['disabled']):
			button.state(['!disabled'])

# Main window object
root = Tk()
root.title("Hangman")

# Change window icon
photo = PhotoImage(file = './hangman/logo.png')
root.wm_iconphoto(False, photo)


# Frame for guessing gui
guessing_frame = ttk.Frame(root, padding=10)


# Callback for button pressed
def on_guess(button, letter):
	count = word.count(letter) # Count how many of the guessed letter is in the word

	button.state(['disabled']) # Disable the button used to guess to prevent duplicate guesses

	if count > 0: # If there is at least 1 of guessed letter in word
		correct_letters.append(letter) # Add to correct letters
		correct_string = get_letters_in_word() # Get correct string
		correct_label.configure(text=correct_string) # Change label
	else: # Guessed letter is not in word
		incorrect_letters.append(letter) # Add to incorrect letters
		incorrect_string = f"Wrong letters: {' '.join(incorrect_letters)}" # Format string
		incorrect_label.configure(text=incorrect_string) # Change label

		# Change the hangman photo
		new_image = PhotoImage(file=f"./hangman/stage_{len(incorrect_letters) + 1}.png")
		hangman_image.config(image=new_image)
		hangman_image.image = new_image

	# Update the count label, show how many of guessed letter is in word
	if count == 1:
		count_label.configure(text=f"The word has 1 {letter}")
	else:
		count_label.configure(text=f"The word has {count} {letter}'s")

	
	check = get_letters_in_word().replace(" ", "") # Get string to validate

	if check == word: # If current guess finishes the word
		end_label.configure(text="You Won!") # Update label to win state
		disable_all_guess_buttons() # Disable buttons so player cannot guess after finishing game
	
	if len(incorrect_letters) == 6: # If guessed incorrectly 6 times aka made full hangman
		end_label.configure(text="You Lost!") # Update label to lose state
		word_label.configure(text=f"The word was: {word}") # Show player the word
		disable_all_guess_buttons() # Disable buttons


# Function for replay button
def replay():
	# Global state variables
	global word, incorrect_letters, correct_letters

	# Refresh word
	response = requests.get(word_site)
	word = response.content.decode('utf-8').replace('[', '').replace(']', '').replace('"', '')

	# Reset state
	incorrect_letters = []
	correct_letters = []

	# Reset labels to default text
	end_label.configure(text="")
	word_label.configure(text="")
	count_label.configure(text="")
	incorrect_label.configure(text="Incorrect letters:")

	# Reset correct label to new word
	guessing = get_letters_in_word()
	correct_label.configure(text=guessing)

	# Enable guessing buttons
	enable_all_guess_buttons()

	# Reset hangman visual
	new_image = PhotoImage(file=f"./hangman/stage_1.png")
	hangman_image.config(image=new_image)
	hangman_image.image = new_image

# Hangman visuals
image = PhotoImage(file="./hangman/stage_1.png")
hangman_image = ttk.Label(root, text="", image=image)

# Label for showing if player won or lost
end_font = font.Font(family="TkHeadingFont", size=40)
end_label = ttk.Label(root, text="", font=end_font)

# Label for if player loses, shows what the word is
word_font = font.Font(family="TkMenuFont", size=20)
word_label = ttk.Label(root, text="", font=word_font)

# Label for showing how many of guessed letter is in word
count_label = ttk.Label(guessing_frame, text="", padding=20)

# Label for showing incorrect guesses
incorrect_font = font.Font(family="TkMenuFont")
incorrect_label = ttk.Label(guessing_frame, text="Incorrect letters:", font=incorrect_font, padding=20)

# Label for showing correct guesses
starting = get_letters_in_word()
correct_font = font.Font(family="TkHeadingFont")
correct_label = ttk.Label(guessing_frame, text=starting, font=correct_font, padding=20)

# Button to reset game
replay_button = ttk.Button(root, text="Replay", command=replay, padding=20)

# Frame to hold all the guessing buttons
button_frame = ttk.Frame(guessing_frame, padding=10)

# All the guessing buttons (idk how to make this more efficient)
a_button = ttk.Button(button_frame, text="A", command=lambda : on_guess(a_button, "a"))
b_button = ttk.Button(button_frame, text="B", command=lambda : on_guess(b_button, "b"))
c_button = ttk.Button(button_frame, text="C", command=lambda : on_guess(c_button, "c"))
d_button = ttk.Button(button_frame, text="D", command=lambda : on_guess(d_button, "d"))
e_button = ttk.Button(button_frame, text="E", command=lambda : on_guess(e_button, "e"))
f_button = ttk.Button(button_frame, text="F", command=lambda : on_guess(f_button, "f"))
g_button = ttk.Button(button_frame, text="G", command=lambda : on_guess(g_button, "g"))
h_button = ttk.Button(button_frame, text="H", command=lambda : on_guess(h_button, "h"))
i_button = ttk.Button(button_frame, text="I", command=lambda : on_guess(i_button, "i"))
j_button = ttk.Button(button_frame, text="J", command=lambda : on_guess(j_button, "j"))
k_button = ttk.Button(button_frame, text="K", command=lambda : on_guess(k_button, "k"))
l_button = ttk.Button(button_frame, text="L", command=lambda : on_guess(l_button, "l"))
m_button = ttk.Button(button_frame, text="M", command=lambda : on_guess(m_button, "m"))
n_button = ttk.Button(button_frame, text="N", command=lambda : on_guess(n_button, "n"))
o_button = ttk.Button(button_frame, text="O", command=lambda : on_guess(o_button, "o"))
p_button = ttk.Button(button_frame, text="P", command=lambda : on_guess(p_button, "p"))
q_button = ttk.Button(button_frame, text="Q", command=lambda : on_guess(q_button, "q"))
r_button = ttk.Button(button_frame, text="R", command=lambda : on_guess(r_button, "r"))
s_button = ttk.Button(button_frame, text="S", command=lambda : on_guess(s_button, "s"))
t_button = ttk.Button(button_frame, text="T", command=lambda : on_guess(t_button, "t"))
u_button = ttk.Button(button_frame, text="U", command=lambda : on_guess(u_button, "u"))
v_button = ttk.Button(button_frame, text="V", command=lambda : on_guess(v_button, "v"))
w_button = ttk.Button(button_frame, text="W", command=lambda : on_guess(w_button, "w"))
x_button = ttk.Button(button_frame, text="X", command=lambda : on_guess(x_button, "x"))
y_button = ttk.Button(button_frame, text="Y", command=lambda : on_guess(y_button, "y"))
z_button = ttk.Button(button_frame, text="Z", command=lambda : on_guess(z_button, "z"))

# Applying grid to all the guessing buttons (pain T-T)
a_button.grid(column=0, row=0)
b_button.grid(column=1, row=0)
c_button.grid(column=2, row=0)
d_button.grid(column=3, row=0)
e_button.grid(column=4, row=0)
f_button.grid(column=5, row=0)
g_button.grid(column=6, row=0)
h_button.grid(column=7, row=0)
i_button.grid(column=0, row=1)
j_button.grid(column=1, row=1)
k_button.grid(column=2, row=1)
l_button.grid(column=3, row=1)
m_button.grid(column=4, row=1)
n_button.grid(column=5, row=1)
o_button.grid(column=6, row=1)
p_button.grid(column=7, row=1)
q_button.grid(column=0, row=2)
r_button.grid(column=1, row=2)
s_button.grid(column=2, row=2)
t_button.grid(column=3, row=2)
u_button.grid(column=4, row=2)
v_button.grid(column=5, row=2)
w_button.grid(column=6, row=2)
x_button.grid(column=7, row=2)
y_button.grid(column=3, row=3)
z_button.grid(column=4, row=3)

# Applying grid to the main game components
button_frame.grid(column=0, row=2, columnspan=8, rowspan=4)
correct_label.grid(column=1, row=0)
incorrect_label.grid(column=2, row=0)
count_label.grid(column=1, row=1)

# Applying grid to the guessing frame (holds all main game guis)
guessing_frame.grid(column=1, row=0)

# Apply grid to hangman visuals
hangman_image.grid(column=0, row=0)

# Apply grid to game end labels
end_label.grid(row=1, column=0)
word_label.grid(row=1, column=1)

# Apply grid to replay button
replay_button.grid(row=1, column=3)


# Run the main window
root.mainloop()