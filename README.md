Tic Tac Toe w/ Machine Learning AI
------
This is a simple Tic Tac Toe game which runs from the command line.  Features a computer AI that plays from an
Artificial Neural Network (ANN).

### Requirements
+ Python 3.6.4
+ PostgreSQL 10
+ Git Version Control (if you want to evaluate changes)

### Python Packages
+ random
+ psycopg2

## Introduction

The goal for this project to solidify basic Python concepts and control structures without introducing too many
libraries.  This version features player vs. two different computer artificial intelligence (AI), named 'Bit' and 'Byte'.

## Discussion

Though this game runs from the command line, with a little bit more work, it can be made to run from a graphical user
interface (GUI) or a web browser.

For a web version of the game, another language, such as Javascript or Ruby, is probably more appropriate.

### Bit: Unbeatable Algorithm

Bit is based on a simple algorithm and is explicitly programmed to choose its moves based on a set of predetermined rules.
Because Tic Tac Toe is a solved game with the winning strategy more narrow compared to a game like chess or Go, an AI
can be efficiently programmed with a few rules to become unbeatable.

### Byte: Self-Learning AI

Byte is a little bit more complex than Bit.  It started off playing terribly, picking random moves, but learns how to
play better every time the game is played. At the start of its turns, Byte retrieves recorded game states for its
possible moves and picks the one with the highest P-value (probability of winning). Byte records the game state of each
turn and adjusts the recorded P-value of each game state at the end of a game based on the outcome. Byte is able to
learn from players and other computer AI.  For it to become unbeatable, it must be "trained" with a large number of
games to develop its neural network (i.e. database of game states and P-values).

Using a ANN to develop AI is probably overkill for a game like Tic Tac Toe.  However, in a simple environment, we know
how its ideal behavior should perform, therefore we can determine if the algorithm is correct.  Because Byte is allowed
self-discovery not given any explicit instruction of how to play, its algorithm can be passed into a more complex game.

## Author
Brandon Yuong

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
+ Book:  Invent Your Own Computer Games with Python (by Albert Sweigart)
+ https://users.auth.gr/kehagiat/Research/GameTheory/12CombBiblio/TicTacToe.pdf