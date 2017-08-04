# AI_Final_Project

#### Project structure

###### RPS.py
The main script that executes game logic.

###### Player.py
Contains implementation for different players.

#### Running the code
```
./RPS.py --player1 playerNumber|h --player2 playerNumber|h --numberOfGames number
```
*Note: options should be necessarily provided 
 
#### Option description

###### player1
Specifies the type of the player for player one. Should be number 0-8 or h (for human player).

###### player2
Specifies the type of the player for player two. Should be number 0-8 or h (for human player).

###### numberOfGames
Specifies how many games will be played.

#### Output
The RPS script outputs three types of logs (as files): generic log, log for player 1, log for player 2. In general logs contain statistics for players and the game in general.
