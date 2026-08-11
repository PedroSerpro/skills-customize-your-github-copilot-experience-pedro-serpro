
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in Python that uses a word list, user input, loops, and conditionals to manage gameplay.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the game by choosing a random secret word and initializing variables to track guesses and game state.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list
- Initialize variables for guessed letters, incorrect guesses, and the maximum allowed mistakes
- Display the current progress of the hidden word in `_ _ _` format

### 🛠️ Guess Handling and Game Flow

#### Description
Implement the main game loop that accepts letter guesses, updates the game state, and ends when the player wins or loses.

#### Requirements
Completed program should:

- Accept a letter guess from the user each turn
- Update and display correct guessed letters in the current word progress
- Track incorrect guesses and remaining attempts
- End the game when the word is fully guessed or the player runs out of tries
- Show a win message when the player guesses the word and a lose message when attempts are exhausted
