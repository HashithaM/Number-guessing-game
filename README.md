# Number-guessing-game
This is a number guessing game using python with two difficulty levels
The game randomly selects a number between 1 and 100, and the player has a limited number of attempts to guess that number. Here's a breakdown of your code:

You import the logo from an art module. Presumably, this logo adds some visual flair to your game.

You define constants EASY_LEVEL_TURNS and HARD_LEVEL_TURNS to determine the number of turns allowed for easy and hard difficulty levels, respectively.

The check_answer function takes the user's guess, the correct answer, and the remaining turns as parameters. It compares the guess with the answer and returns the updated number of turns.

The set_difficulty function prompts the user to choose a difficulty level (easy or hard) and returns the corresponding number of turns.

The game function initializes the game, generates a random number as the answer, sets the difficulty level, and starts the game loop. Inside the loop, it prompts the user for a guess, checks the guess using the check_answer function, and updates the number of turns accordingly. If the user runs out of turns, the game ends.

Finally, you call the game function to start the game.
