Tic Tac Pong devlog #06
<br> 
18/10/2026 | jdo1-des 
<br> 
![screenshot of the pong screen showcasing power ups](https://github.com/jdo1-des/Tic-Tac-Pong/blob/598d238a3dd7032495403e010dda6ab7fc0739d5/power%20up%20on%20screen.jpg)<br>
TLDR: added 3 power ups to spice up gameplay. There a 3 types, a ball speed up, an opponent paddle slow down, and a lengthen to ur won paddle
<br>
I added a new feature to my game, power ups! These help spice up the game play adn make each pong rally less repitive. To activate hit a green blob that randomly spawns on screen.
I made the blob large as in playtesting I found it could be hard to hit it. But I wanted it to be hit often as rallies are quite short.
There are 3 types of power ups speed up, lengthen, and slow down. Speed up increases the balls speed. Lengthen makes the player who last hit the balls paddle longer.
Slow down decreases the player who didn't just hit the ball paddle speed.The hardest of these to add was by far the lenghten ability. This was because I had to redraw 1 paddle, 
every time the ball was hit. To make it work I added a new function to the paddle.py file. This redraws the paddle but longer when a power up is activated.
<br>
Completed: <br>
power ups
