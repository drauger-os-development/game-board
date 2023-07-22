# game-board
On-screen keyboard featuring a dual-radial layout. Designed for use with XBox, PlayStation, or Nintendo Switch controllers.

# About
`game-board` uses the `pygame` library to provide the GUI and hardware interface. `game-board` is still very much in the early development stages and not yet ready for use.

# Platform Support
`game-board` will initially support Linux, but support for Mac OS and Windows is planned.

# Controller Support

Currently, `game-board` supports Xbox 360, PS3, PS4, and Nintendo Switch controllers. Xbox One controllers are strongly expected to work, but have not been tested. It is unknown whether PS2, PS5, or Xbox Series X/S controllers work. If you have a controller for one of these consoles, and would like to test it, please create an issue report and we will be happy to walk you through what to do.

# Development
If you wish to help develop `game-board`, there are a few requirements:

**A) Knowledge of Python and Pygame**
 
 `game-board` is written entirely in Python, and heavily leverages the `pygame` library to provide services. Experience with these is a must.
 
**B) Some form of gamepad**

In order to test your code in the real world, you need some form of gamepad. This can be XBox (any generation), PlayStation 3/4, Nintendo Switch, or a generic gamepad with a similar layout and control scheme to any of the mentioned ones.

If your controller does not automatically register as an Xbox, PS3, PS4, or Switch controller, try adding it to `overrides.py` and specifying what it should be recognized as.


## Known issues

**A) Selected slices do not match up with Joystick location**

This is currently being investigated

**B) Right radial menu does not change in response to left radial menu selection**

This is not yet implemented.

**C) Custom layouts are not working**

This is not yet implemented.

**D) Characters are not shown on screen**

This is not yet implemented.

**E) There is no input from `game-board`**

This is not yet implemented.

**F) Buttons do nothing**

This is not yet implemented.