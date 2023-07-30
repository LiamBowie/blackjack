**README.md**

# Blackjack Project

![image](https://github.com/LiamBowie/blackjack/assets/15195267/ea73f259-ec6a-47cf-9719-6281df155de3)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Game Rules](#game-rules)
- [Features](#features)
- [Examples](#examples)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

"Blackjack" is a Python command-line application that allows you to play the classic card game with multiple players. The project was created as a way to practice Object-Oriented Programming and inheritance skills.

## Installation

To run the "Blackjack" project on your local machine, follow these steps:

1. Clone the repository to your local machine: `git clone https://github.com/your-username/blackjack.git`
2. Navigate to the project directory: `cd blackjack`

**Option 1:** Run the program using the Python script:

3. Execute the script: `python3 script.py`

**Option 2:** Run the program using the downloaded distribution:

3. Navigate to the "dist/script" folder: `cd dist/script`
5. Run the script: `./script.exe` (or `script.exe` on Windows)

## Game Rules

In "Blackjack," you can choose the number of players sitting at the table, all controlled by the same command line instance. Each player starts with 100 chips and can bet on each hand of blackjack.

The game follows standard blackjack rules with the following features:

- There is no minimum bet, as long as it is above 0 and less than the total number of chips available.
- During the first turn, a player can choose to "twist" to get another card or "stand" to keep their current hand and move on to the next player.
- If a player has enough chips, they can "double down" on their first turn and receive one extra card.
- If a player's initial hand contains two cards of the same value, they can "split" their hand into two separate hands, provided they have enough chips to match their original bet.
- Players can continue to split their hands and double down if all the requirements are met.
- Soft aces and hard aces are implemented, where the first ace in a hand counts as 11, and any subsequent aces count as 1. If a player goes bust with an ace valued at 11, the value of their hand will be reduced by 10 so that all aces in the hand count as 1.

Once all hands have been played, the dealer takes their turn by twisting until they reach a hand value of 17 or above.

## Features

- **Multiple Players:** Play with any number of players at the table, all controlled through the command line.
- **Betting System:** Each player starts with 100 chips and can bet on each hand of blackjack.
- **Double Down:** Players can double their initial bet and receive one additional card on their first turn.
- **Splitting Hands:** If a player's initial hand contains two cards of the same value and they have enough chips, they can split their hand and play two separate hands.
- **Soft Aces:** Aces in a hand are counted as 11 if they don't cause the player to go bust; otherwise, they are counted as 1.

## TODO: Examples

## Dependencies

The "Blackjack" project requires the following Python standard libraries:

- os
- random
- abc

## Contributing

Contributions to the "Blackjack" project are welcome! If you find any issues or have suggestions for improvements, please submit a pull request.

## TODO: Licensing
