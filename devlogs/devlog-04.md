Tic Tac Pong devlog #04
<br> 
17/10/2026 | jdo1-des 
<br> 
![screenshot of tic tac toe board after a player has won]([https://github.com/jdo1-des/Tic-Tac-Pong/blob/65df9d47f774496b4c9a7378c7fe909a262763e3/Screenshot%202026-10-17%20105152.jpg](https://github.com/jdo1-des/Tic-Tac-Pong/blob/70e83c70af946a04ed74dd2b2db3d6ddef198b7e/Screenshot%202026-10-17%20131732.jpg))
<br>
TLDR: finished the tic tac toe game. The game is now fully playable.
<br>
I have somewhaty completed the game now. I completed the tic tac toe part so it now knows if a player has got 3 in a line and won. 
The tic tac toe also closes after a marker is palced and goes back to the pong game. This cycle continues until the tic tac toe game has been won by a player.
The hardest part was getting the game to remember the board after each round, so it wouldn't reset. 
This was hard as the board was stored as a matrix so I couldn't send it across the files using the Popen and sys.executable like I did for the round winner.
Instead I used the pickle library to convert the matrix to bytes and decode them once they were sent across. I choose pickle as it better for saving more complex data types like matrixs than alternatives such as JSON.
While the game is playable, I am not finished yet. I plan to go through my code and optomize it where possible so the game will run smoother and faster.
<br>
Completed: <br>
After a marker is placed pong game restarts <br>
Check if someone has won tic tac toe <br>
Next steps: <br>
Optimize code
