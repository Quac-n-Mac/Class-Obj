import pgzrun, random

WIDTH=1300
HEIGHT=800

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

GRAVITY = 2000.0

class Ball:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.vx=random.randint(175, 225)
        self.vy=0
        self.radius=random.randint(30,120)
    def balldraw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, (r,g,b))

ball1 = Ball(250,250)
ball2 = Ball(120,120)

def draw():
   screen.clear()
   ball1.balldraw()
   ball2.balldraw()

def update(dt):

    uy = ball1.vy
    ball1.vy += GRAVITY * dt
    ball1.y += (uy + ball1.vy) * 0.5 * dt
    if ball1.y > HEIGHT-ball1.radius:
        ball1.y = HEIGHT-ball1.radius
        ball1.vy = -ball1.vy*0.85
    if ball1.y < 0+ball1.radius:
        ball1.y = 0+ball1.radius
        ball1.vy = -ball1.vy*1.05
    if ball1.x > WIDTH-ball1.radius or ball1.x < 0+ball1.radius:
        ball1.vx = -ball1.vx
    ball1.x += ball1.vx*dt

    uy = ball2.vy
    ball2.vy += GRAVITY * dt
    ball2.y += (uy + ball2.vy) * 1 * dt
    if ball2.y > HEIGHT-ball2.radius:
        ball2.y = HEIGHT-ball2.radius
        ball2.vy = -ball2.vy*1
    if ball2.y < 0+ball2.radius:
        ball2.y = 0+ball2.radius
        ball2.vy = -ball2.vy*1.10
    if ball2.x > WIDTH-ball2.radius or ball2.x < 0+ball2.radius:
        ball2.vx = -ball2.vx*1.2
    ball2.x += ball2.vx*dt

def on_key_down(key):
    if key==keys.LEFT:
        ball1.vy = -600
    if key==keys.RIGHT:
        ball2.vy = -900

pgzrun.go()