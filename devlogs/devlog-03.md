Tic Tac Pong devlog #03
<br> 
17/10/2026 | jdo1-des 
<br> 
![screenshot of tic tac toe board](https://github.com/jdo1-des/Tic-Tac-Pong/blob/65df9d47f774496b4c9a7378c7fe909a262763e3/Screenshot%202026-10-17%20105152.jpg)
<br>
TLDR: started progress on the tic tac toe game and implemented system that makes winner of pong the player in tic tac toe.
<br>
I have started working on the 2nd half of my game, the tic tac toe. 
So far I have made the board open in a new window after the pong game is done, and the player who won can place a marker (X  for player 1 and O for player 2). 
Currently there is no win condition for the tic tac toe, and no limit to how many markes the winner can place. So the winner can fill the board with markers but nothing will happen. 
I also had to slow the pong ball down, as it was too fast and sometimes impossible for the player it went towards at the start to block it. 
A bug I encountered while making the grid for the board was the lines didn't show up. It took me a while to work it out, 
but it was because I had set the line's colour as a constant and the constant had the same colour value as the background. Once I did find the error it was easy to fix. 
Another issue I had was with getting the tic tac toe board to open, in the pong file I had a typo around the exectuable to open the other file. I had fat finger a '=' where there should have been a bracket. 
This was a quick fix, but it took a while to indetify and find the issue. 
My next steps are to have the pong game restart when a marker is placed on the board and add a system to check if the tic tac toe has a winner yet.
<br>
Completed: <br>
Tic tac toe board <br>
Winner of pong palces the marker <br>
Next steps: <br>
After a marker is placed pong game restarts <br>
Check if someone has won tic tac toe <br>

