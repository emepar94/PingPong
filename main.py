from pygame import *

#window
window_heigh = 960
window_width = 1280

window = display.set_mode((window_width, window_heigh))
display.set_caption("Ping Pong")
background = (255, 255, 255)
window.fill(background)

clock = time.Clock()
FPS = 190

game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

    display.update()
    clock.tick(FPS)
