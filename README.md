# Mastermind
* Master Mind is a code-breaking game
* text-based program using command lines

# Implematations

* Use the digists 1 to 8 instead of colours.
* The game (codemaster) will generate a random 4-digit code, e.g. 2641.
    - We keep things simpler by not allow duplicate digits in the created code that must be guessed.
* The player (codebreaker) gets 12 turns to guess the 4 digits.
    - The player must enter 4 digits.
    - The game indicates (a) how may are correct digit and in correct place, or (b) correct digit, but not in the correct place

# Program

* Generate a random 4-digit code.
* Repeatedly get user input and evaluate.
* Calculate correctness of digits in guess.
* Output results.
