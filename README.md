# ARCADE GAME - Brick Breaker

This is an arcade game in Python3 (terminal-based), of brick breaker game. In this the player operates the paddle to bounce the ball to destroy the bricks.

## Installation

Colorama library:
```
pip3 install colorama
```
Numpy library
```
pip3 nstall numpy
```
## Run
```
python3 main.py
```

## Rules and Features


- Player has one paddle. In the starting the player can control the ball release.Ball respawns on randomn spot on the Paddle

- Player loose a life on when ball goes below the paddle or touches the ground

- After the ball get released. If it collides with wall it get delflected by wall in the opposite direction.

- If the ball collides with bricks, bricks looses its strength changes its color and reflect the ball.

- Player gets points on hitting the brick.

- If the ball collides with the paddle it will get deflected acoording to the position of paddle.

- The colors of the bricks are according to strength. 
WHITE - 1, YELLOW - 2, BLUE - 3, RED - Unbreakable, GREEB - Explosive



## Concept Used

The main concept used in this OOPS concept.

### Inheritance

Classes in bricks.py inherit from the parent class Brick.

### Polymorphism

Functions such as  in powerups uses polymorphism.


### Abstraction

Functions such as addPowrups(), checkCollision(), moveBall() in Ball uses.

### Encapsulation

Classes and objects based approach is used which makes this program more modular and hence encapsulation is used in this.

## Powerups implemented

### long paddle 
### short paddle 
### thru Ball 
### Fast Ball
### Ball grab 

## Controls

### `D`: Move Right

### `A`: Move Left

### `q` or `Q` - Quit the game.

### `u` - release the ball.