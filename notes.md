# [Build a Python Turtle Game: Space Invaders Clone](https://realpython.com/build-python-turtle-game-space-invaders-clone/)

## Prerequisites

* https://realpython.com/beginners-guide-python-turtle/

> You can always stop and review the resources linked here if you get stuck.

## Step 1

### Create the Screen

### Create the Laser Cannon

> The center of the screen has the coordinates `(0, 0)`.

## Step 2

### Move the `turtle` Object

对于游戏引擎来说，处理键盘按键比处理鼠标的移动和点击更容易

> By default, the `turtle` module doesn’t use computing resources to listen for keypresses while the program is running. Calling `window.listen()` overrides this default.

> Functions used as arguments for `.onkeypress()` can’t accept any required arguments. Although the functions can have a `return` statement, you can’t access the returned data in your program since these functions are called from within `.onkeypress()`.

## Step 3

### Create Lasers

To avoid complicating the code, this tutorial makes some simplifications:
1. The height of the cannon is hardcoded to 20 pixels. This value is used in `draw_cannon()` to place the rectangles that make up the cannon, and in `create_laser()`, to place the laser’s starting point at the tip of the cannon. In general, you should try to avoid hardcoding values. This value could be defined as a percentage of the screen height, and the appropriate changes made to `draw_cannon()` to set the widths and heights of the three rectangles used to draw the cannon.
2. The function `create_laser()` modifies a list in the program’s global scope. In general, it’s best for functions to return values instead of changing the state of existing global variables. However, you’ll call `create_laser()` through a keypress, and this prevents you from accessing the returned objects.

### Create the Game Loop to Move the Lasers

> Each iteration of the game loop represents a frame of the game.

> A turtle program runs an event loop, which starts when you call `turtle.done()` and handles events such as keypresses.

But the `turtle.done()` call is outside the `while` loop, so its unreachable.
The program still works after removing the call.

But later in Step 6 when we exit the `while` loop, this call will be needed again.

> You can compare the game loop you’ll need when working with `turtle`, to the game loop structures in other Python games packages such as `pygame` and `arcade`.

按住空格连续发射大量子弹，可以看到性能的下降，当子弹离开屏幕从而被移除时，性能又重新回升

## Step 4

### Spawn New Aliens

### Move the Aliens

> If the aliens aren’t moving at the right speed, you can adjust their speed by using a different value for `ALIEN_SPEED`. Keep in mind that the speed of the game will vary depending on the system you’re working on. You’ll set the frame rate of the game in the last step of this tutorial, so you don’t need to worry about the speed for now.

## Step 5

## Step 6

## Step 7

## Step 8

> If you want the cannon to have a smoother motion, you need to move it in smaller increments continuously.

> A data attribute is similar to a variable, but it’s attached to an object.
> The `Turtle` object already has other data attributes defined in the Turtle class,
> but `.cannon_movement` is a custom data attribute you add in your code.
> 
> The reason you need to use a data attribute instead of a standard variable is
> so you can modify its value within functions.
> If you define a standard variable for this value,
> the functions `move_left()` and `move_right()` would need to return this value.
> But these functions are bound to keys, and they’re called from within `.onkeypress()`,
> so you can’t access any data they return.

> The game works perfectly. However, if you try to run this game on different computers, you’ll notice that the speed of the game varies. To account for this, you may need to adjust the speed values for the cannon, laser, and aliens depending on the kind of computer running the game.
> 
> In the final step of this tutorial, you’ll set the game’s frame rate so that you can control how fast the game runs on any computer.

## Step 9

> As long as the time it takes to run the `while` loop is shorter than the time required for one frame, every frame will take the same amount of time once the pause is completed.

## Next Steps

* **Add difficulty levels**: You can increase the speed of the aliens and the spawn rate after a certain time interval has passed, or once you destroy a certain number of aliens. This will make the game progressively harder.
* **Limit the number of lasers**: Set a limit on how many lasers are available so you only get a top-up after a certain amount of time has passed, or when you destroy a certain number of aliens. That’s the end of keeping the spacebar pressed down!
* **Create a fixed-cannon version**: Modify the game so that the cannon doesn’t move but can rotate when you press the arrow keys to shoot in different directions. This makes for a fun variation of the game.