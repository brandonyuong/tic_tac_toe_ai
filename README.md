Tic Tac Toe w/ Machine Learning AI
------
This is a simple Tic Tac Toe game which runs from the command line.  Features a machine learning AI that plays from an
Artificial Neural Network (ANN).

### Requirements
+ Python 3.6.4
+ PostgreSQL 10 (only for training the AI. Not required to execute program)
+ Git Version Control (if you want to evaluate changes)

### Python Packages
+ random
+ psycopg2

## Author
Brandon Yuong

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
+ Book:  Invent Your Own Computer Games with Python (by Albert Sweigart)
+ Paper:  https://users.auth.gr/kehagiat/Research/GameTheory/12CombBiblio/TicTacToe.pdf

## Introduction

The goal for this project is to:

1.  Solidify basic Python concepts and control structures without introducing too many libraries.
2.  Create an unbeatable computer opponent.

This version features player vs. two different computer artificial intelligence (AI) algorithms, named 'Bit'
and 'Byte'.

## Helping

+ Byte, the machine learning AI, is currently unbeatable as far as I am aware.  If you beat it repeatedly, or
consistently please let me know what you did!
+ Suggestions to how I can clean the code better is welcome!
+ Please let me know if you know of any bugs.  Thanks!

## Discussion

Though this game runs from the command line, with a little bit more work, it can be made to run from a mobile app via a
graphical user interface (GUI) or a web browser.

Any of these options may or may not require a different language than Python that is more appropriate, depending on the
environment.

### Bit: Unbeatable AI?  Almost

Bit is based on a simple algorithm and is explicitly programmed to choose its moves based on a set of predetermined rules.
Because Tic Tac Toe is a solved game with the winning strategy more narrow compared to a game like chess or Go, an AI
can be efficiently programmed with a few rules to become convincing and seemingly unbeatable.

#### What's the catch?

If someone studies the rules of the algorithm, it is certainly possible to find exploits and beat the AI.  The counter
to this would be to add more rules and contingencies.  Therefore, the competence of the AI is dependent on:
1.  More time testing and writing code.
2.  The competence of the developer.

#### Scaling Matters

For a game that is more complex than Tic Tac Toe, that would require the developer to be or become very competent at the
game, i.e. spend time understanding and developing strategies to play the game.  Even then, there would be no guarantee
that the AI algorithm will be unbeatable.  In other words, a world champion chess AI would need a world champion
chess-playing developer.

### Byte: The Self-Learning AI

Byte is a little bit more complex than Bit.  It initially played terribly, picking random moves, but learns how to
play better every time the game is played.  At the start of its turns, Byte retrieves recorded game states for its
possible moves and picks the one with the highest P-value (probability of winning).

#### Machine Learning

Though machine learning is involved, Byte is not told what actions to take, but instead learns what actions achieves
the goal of winning and avoiding losses.  It does not repeat its mistakes (if the method to record is enabled).
This can be said to be a simple illustration of reinforcement learning.

After a few training iterations, I started to learn from the AI of how to play Tic Tac Toe better!

#### How Byte Works

Byte records the game state of each turn and adjusts the recorded P-value of each game state at the end of a game based
on the outcome. Byte is able to learn from players and other computer AI.  For it to become unbeatable, it must be
"trained" with a large number of games to develop its neural network (i.e. database of game states and P-values).

#### How It Is Efficient

In a simple environment, we know its ideal behavior and how it should perform, therefore we can determine if the
algorithm is correct.  Because Byte is allowed self-discovery and does not require explicit instruction of how to play,
its algorithm can be passed into a more complex game that has finite states and rules.

Byte's algorithm is dynamic and can adapt to stronger opponents or opponents playing unorthodox or rogue strategies
against it.  Strategy discovery is built into its algorithm.  It is truly able to become an unbeatable AI in Tic Tac Toe!