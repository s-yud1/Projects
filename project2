import turtle
import random
import math

# --- Screen setup ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)  # turn off animation for smooth movement

# --- Create particles ---
particles = []
for _ in range(25):  # number of particles
    t = turtle.Turtle()
    t.shape("circle")
    t.shapesize(0.5)  # make them smaller
    t.color(random.choice(["cyan", "magenta", "yellow", "white"]))
    t.penup()
    t.speed(0)
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    particles.append(t)

# --- Track mouse position ---
cursor_x, cursor_y = 0, 0
def update_cursor(x, y):
    global cursor_x, cursor_y
    cursor_x, cursor_y = x, y

# you can use onscreenclick or onmousemove
screen.onscreenclick(update_cursor)
# for real-time motion tracking, replace above with:
# screen.ontmousemove(update_cursor)

screen.listen()

# --- Animation loop ---
def animate():
    for p in particles:
        x, y = p.position()
        dx = cursor_x - x
        dy = cursor_y - y
        angle = math.atan2(dy, dx)
        dist = math.hypot(dx, dy)
        step = max(1, dist / 30)

        # --- repel particles from each other ---
        repel_x, repel_y = 0, 0
        for other in particles:
            if other is not p:
                ox, oy = other.position()
                d = math.hypot(ox - x, oy - y)
                if d < 30 and d > 0:  # repel when too close
                    repel_x -= (ox - x) / d
                    repel_y -= (oy - y) / d

        # combine attraction to cursor and repulsion
        move_x = math.cos(angle) * step + repel_x
        move_y = math.sin(angle) * step + repel_y

        p.setheading(math.degrees(math.atan2(move_y, move_x)))
        p.goto(x + move_x, y + move_y)

        # optional: glowing trail
        if random.random() < 0.05:
            p.color(random.choice(["cyan", "white"]))

    screen.update()
    screen.ontimer(animate, 20)

animate()
turtle.done()
