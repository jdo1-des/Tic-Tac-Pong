Tic Tac Pong devlog #04
<br> 
17/10/2026 | jdo1-des 
<br> 
![screenshot of the pong screen showcasing the round counter and start of game countdown](https://github.com/jdo1-des/Tic-Tac-Pong/blob/fbdd99dd615ec10d582fd21de27b67c4d60bddc6/coloured%20paddles.jpg)
![screenshot of the tic tac toe screen showcasing the coloured markers and round counter](https://github.com/jdo1-des/Tic-Tac-Pong/blob/fbdd99dd615ec10d582fd21de27b67c4d60bddc6/colourd%20tic%20tac%20toe.jpg)
<br>
TLDR: Coloured the paddles and markers, added a round counter at the top of the screen, added a 3 second countdown before a pong rally starts, optimized and conventionalized code.
<br>
I changed the colours of the paddles and markers so Player A's (X and left paddle) are now red. Player B (O and right paddle) is blue. 
This makes it easy for players to remember what paddle/markers are theirs. At the top of the screen there is now a round counter. 
It is now possible for players to tie, if the tic tac toe board is filled but their is not winner. I changed the balls start velocity so it has an even chance to go to either side, 
before it would only go right. This maeks the game more fair and random. There is now a 3 second countdown before the start of each rally. 
I had some troubles where the countdown would flicker on the screen. But I fixed this by moving all the countdown code from a for into a while loop.
This meant only the countdown would run, so nothing else was drawn over it. I fixed some errors witht eh variable and Cconstant names in my code. 
There where a lot of constants not all caps, so I went through and made them all caps to conventionalize my code.
I also patched an error where the tic tac toe would run if the pong fiel was launched outside a coed studio. This happened because in the code studio the files were all in the smae directory.
But if you launched them directly they could be in different directories. To fix it I simpled had the files search for eachother before the game started, and saved their locations as variables to use later.
Next I might add some power ups to spice up the gameplay. Power ups I have in mind are speeding up the ball for a short time, extending the paddle, and slowing down the opponent's paddle.
<br>
Completed: <br>
Round counter<br>
Coloured paddles and markers<br>
Rally countdown <br>
optimized code<br>
Next steps: <br>
add power ups
