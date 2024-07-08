import random
import time
import turtle

CANNON_STEP = 10
LASER_LENGTH = 20
LASER_SPEED = 0.5
ALIEN_SPAWN_INTERVAL = 1.2  # seconds
ALIEN_SPEED = 0.05

window = turtle.Screen()
window.tracer(0)
window.setup(0.5, 0.75)
window.bgcolor(0.2, 0.2, 0.2)
window.title("The Real Python Space Invaders")

LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_height() / 2
BOTTOM = -window.window_height() / 2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * window.window_width()

# create laser cannon
cannon = turtle.Turtle()
cannon.penup()
cannon.color(1, 1, 1)
cannon.shape("square")
cannon.setposition(0, FLOOR_LEVEL)

lasers = []
aliens = []

def draw_cannon():
    cannon.clear()
    cannon.turtlesize(1, 4)  # base
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 10)
    cannon.turtlesize(1, 1.5)  # next tier
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 20)
    cannon.turtlesize(0.8, 0.3)  # Tip of cannon
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL)
    window.update()

def move_left():
    new_x = cannon.xcor() - CANNON_STEP
    if new_x >= LEFT + GUTTER:
        cannon.setx(new_x)
        draw_cannon()

def move_right():
    new_x = cannon.xcor() + CANNON_STEP
    if new_x <= RIGHT - GUTTER:
        cannon.setx(new_x)
        draw_cannon()

def create_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color(1, 0, 0)
    laser.hideturtle()
    laser.setposition(cannon.xcor(), cannon.ycor())
    laser.setheading(90)
    # move laser to just above cannon tip
    laser.forward(20)
    # prepare to draw the laser
    laser.pendown()  # draw lines when it moves
    laser.pensize(5)  # lines are 5 pixels wide

    lasers.append(laser)

def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)

def create_alien():
    alien = turtle.Turtle()
    alien.penup()
    alien.turtlesize(1.5)
    alien.setposition(
        random.randint(
            int(LEFT + GUTTER),
            int(RIGHT - GUTTER)
        ),
        TOP,
    )
    alien.shape("turtle")
    alien.setheading(-90)
    alien.color(random.random(), random.random(), random.random())

    aliens.append(alien)

def remove_sprite(sprite, sprite_list):
    sprite.clear()
    sprite.hideturtle()
    window.update()
    sprite_list.remove(sprite)
    turtle.turtles().remove(sprite)

window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(create_laser, "space")
window.onkeypress(turtle.bye, "q")
window.listen()

# draw cannon at start of game
draw_cannon()

# game loop
alien_timer = 0
while True:
    # move all lasers
    for laser in lasers.copy():
        move_laser(laser)
        # remove laser if it goes off screen
        if laser.ycor() > TOP:
            remove_sprite(laser, lasers)
            break
        # check for collision with aliens
        for alien in aliens.copy():
            if laser.distance(alien) < 20:
                remove_sprite(laser, lasers)
                remove_sprite(alien, aliens)
                break
    # spawn new aliens when time interval elapsed
    if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
        create_alien()
        alien_timer = time.time()
    # move all aliens
    for alien in aliens:
        alien.forward(ALIEN_SPEED)

    window.update()
