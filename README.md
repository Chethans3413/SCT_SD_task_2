# Guess the Number Game

## Overview
A simple Python-based number guessing game that challenges users to guess a randomly generated number between 1 and 100. The program provides helpful feedback ("Too low!" or "Too high!") to guide the player toward the correct answer.

## Language
- **Language:** Python 3.x

## Features
- **Random Number Generation:** Generates a random number between 1 and 100 at game start
- **Interactive Guessing:** User enters guesses one at a time
- **Real-time Feedback:** Displays "Too low!" or "Too high!" based on each guess
- **Input Validation:** Handles non-numeric input gracefully with error messages
- **Simple Design:** Clean, straightforward code without external dependencies

## How to Run

### Prerequisites
- Python 3.x installed on your system

### Execution
1. Open a terminal/command prompt
2. Navigate to the project directory:
   ```bash
   cd d:\SCT_SD_task_2
   ```
3. Run the program:
   ```bash
   python guessing_game.py
   ```

## How to Play
1. The program will announce: "I have picked a number between 1 and 100."
2. Enter your guess when prompted
3. The game will respond with:
   - "Too low! Try again." - Your guess is below the secret number
   - "Too high! Try again." - Your guess is above the secret number
   - "Correct! You got it." - You found the correct number!
4. The game ends when you guess correctly

## Example Game Flow
```
I have picked a number between 1 and 100.
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Too high! Try again.
Enter your guess: 31
Too low! Try again.
Enter your guess: 34
Too low! Try again.
Enter your guess: 35
Correct! You got it.
```

## Code Features
- **One-time Number Generation:** The secret number is generated once before the loop starts
- **Error Handling:** Non-numeric input triggers a friendly error message asking for digits only
- **Clean Loop:** Uses `break` to exit when the correct answer is guessed
- **Debug Option:** An optional debug line can be uncommented in the code to reveal the answer for testing

## File Structure
```
d:\SCT_SD_task_2\
├── guessing_game.py    # Main game program
└── README.md           # This file
```

## Tips for Playing
- **Use Binary Search:** Start with 50 to eliminate half the possibilities each time
- **Track Your Guesses:** Keep mental notes of what you've tried to narrow down the range
- **Adapt Strategically:** Use the feedback to adjust your next guess accordingly

## Requirements
- Python 3.x
- No external libraries required (uses only built-in `random` module)

## Support
For issues, ensure you have Python installed and run the program from the correct directory.
