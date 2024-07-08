# Turtle Space Invaders Clone

## https://realpython.com/build-python-turtle-game-space-invaders-clone/

### Prerequisites

* https://realpython.com/beginners-guide-python-turtle/

> You can always stop and review the resources linked here if you get stuck.

### Step 1

#### Create the Screen

#### Create the Laser Cannon

> The center of the screen has the coordinates `(0, 0)`.

### Step 2

#### Move the `turtle` Object

对于游戏引擎来说，处理键盘按键比处理鼠标的移动和点击更容易

> By default, the `turtle` module doesn’t use computing resources to listen for keypresses while the program is running. Calling `window.listen()` overrides this default.

> Functions used as arguments for `.onkeypress()` can’t accept any required arguments. Although the functions can have a `return` statement, you can’t access the returned data in your program since these functions are called from within `.onkeypress()`.
