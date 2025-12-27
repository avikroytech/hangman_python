# Hangman Game

A Python implementation of the classic Hangman word-guessing game with both command-line and graphical user interface (GUI) versions.

## Features

- **Two Game Modes:**
  - **CLI Version** (`hangman.py`) - Play using keyboard input in the terminal
  - **GUI Version** (`hangman_app.py`) - Play with an interactive graphical interface and clickable buttons

- **Random Word Generation** - Fetches random words from the [Random Word API](https://random-word-api.vercel.app/)

- **Game Mechanics:**
  - Guess letters one at a time
  - Track correct and incorrect guesses
  - Visual hangman progression with ASCII art (CLI) or PNG images (GUI)
  - Win condition: Guess all letters before 6 incorrect guesses
  - Lose condition: 6 incorrect guesses completes the hangman

- **Replay Functionality** - Start a new game without restarting the application

- **Responsive UI** - Real-time feedback on guesses with letter counts and visual updates

## Requirements

- Python 3.6+
- `requests` library for API calls
- `pynput` library (for CLI version keyboard input)
- Tkinter (usually included with Python)

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install requests pynput
```

3. Ensure the `hangman/` directory contains the required image files:
   - `logo.png` - Window icon
   - `stage_1.png` through `stage_7.png` - Hangman progression images (PNG format)

## Usage

### GUI Version (Recommended)

```bash
python hangman_app.py
```

**How to play:**
- Click on letter buttons to make guesses
- Watch the hangman image update with each incorrect guess
- Click the **Replay** button to start a new game
- Game displays the word when you lose
- Win by revealing all letters before 6 incorrect guesses

### CLI Version

```bash
python hangman.py
```

**How to play:**
- Press keys on your keyboard to guess letters
- Press `ESC` to exit the game

## Project Structure

```
hangman_python/
├── hangman_app.py      # GUI-based game (Tkinter)
├── hangman.py          # Terminal-based game
├── hangman/            # Game assets
│   ├── logo.png        # Window icon
│   ├── stage_1.png     # Hangman visual progression
│   ├── stage_2.png
│   ├── stage_3.png
│   ├── stage_4.png
│   ├── stage_5.png
│   ├── stage_6.png
│   └── stage_7.png
└── README.md           # This file
```

## Technologies Used

- **Python 3** - Programming language
- **Tkinter** - GUI framework (built-in with Python)
- **Requests** - HTTP library for API calls
- **Pynput** - Keyboard input handling (CLI version)

## Game Rules

1. A random word is selected at the start of each game
2. You have 6 incorrect guesses before the game ends
3. Guess letters by clicking buttons (GUI) or pressing keys (CLI)
4. Correct guesses reveal the letter's position(s) in the word
5. Incorrect guesses add to the hangman drawing
6. **Win:** Guess all letters in the word
7. **Lose:** Make 6 incorrect guesses

## Future Enhancements

- Difficulty levels (easy, medium, hard)
- Score/statistics tracking
- Custom word lists
- Multiplayer mode
- Sound effects and animations

---

Enjoy playing Hangman!