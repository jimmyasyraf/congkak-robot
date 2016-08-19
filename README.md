# congkak-robot
This is the sourcecode for my congkak robot, a robot that plays congkak - a south east asian traditional game. 
The robot is based of Lego Mindstorms EV3 booted in an EV3dev distribution of linux and coded in Python.


# How to operate
Graphical
1. Boot up the EV3 brick.
2. Navigate to File Browser
3. Click robot_congkak.py

Command line
1. Press CTRL-ALT-F6 to open the terminal
2. python robot_congkak.py

# The game
It is a human vs machine game so there will be alternate turns. The game starts with the human's turn.
1. The game starts off with the robot calibrating to the right.
2. Press the touch sensor and start picking the balls from one of the hole from your side and distribute. The robot detects your hand and does the calculation on the background.
3. If you end up in your 'home' hole, press the touch sensor and to begin your next turn.
4. If you die, press the touch sensor and the robot will starts its turn.
5. When the robot's turn ended, press the touch sensor to begin your next turn.
6. The cycle continues until the game ends.

#Troubleshooting
Sometimes the motors do not run. For some reasons, just run ev3_motor.py once and then run the file you wanted. It should work after that.

