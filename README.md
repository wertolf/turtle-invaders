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

### Step 3

#### Create Lasers

To avoid complicating the code, this tutorial makes some simplifications:
1. The height of the cannon is hardcoded to 20 pixels. This value is used in `draw_cannon()` to place the rectangles that make up the cannon, and in `create_laser()`, to place the laser’s starting point at the tip of the cannon. In general, you should try to avoid hardcoding values. This value could be defined as a percentage of the screen height, and the appropriate changes made to `draw_cannon()` to set the widths and heights of the three rectangles used to draw the cannon.
2. The function `create_laser()` modifies a list in the program’s global scope. In general, it’s best for functions to return values instead of changing the state of existing global variables. However, you’ll call `create_laser()` through a keypress, and this prevents you from accessing the returned objects.

#### Create the Game Loop to Move the Lasers

> Each iteration of the game loop represents a frame of the game.

> A turtle program runs an event loop, which starts when you call `turtle.done()` and handles events such as keypresses.

But the `turtle.done()` call is outside the `while` loop, so its unreachable.
The program still works after removing the call.

> You can compare the game loop you’ll need when working with `turtle`, to the game loop structures in other Python games packages such as `pygame` and `arcade`.

按住空格连续发射大量子弹，可以看到性能的下降，当子弹离开屏幕从而被移除时，性能又重新回升
