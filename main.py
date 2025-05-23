from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pos_x, pos_y, size_x, size_y, speed, picture):
        super().__init__()
        self.image = transform.scale(image.load(picture), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = pos_x
        self.rect.y = pos_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

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
