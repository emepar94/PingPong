import time
from time import sleep

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

class Player(GameSprite):
    def UpdateLeft(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < window_heigh-50:
            self.rect.y += self.speed
    def UpdateRight(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < window_heigh - 50:
            self.rect.y += self.speed

# window
window_heigh = 650
window_width = 1280

window = display.set_mode((window_width, window_heigh))
display.set_caption("Ping Pong")
background = transform.scale(image.load("background.png"), (window_width, window_heigh))

clock = time.Clock()
FPS = 60

# text
font.init()
font1 = font.Font(None, 80)

# exemplare
RocketLeft = Player(5, window_heigh/2 - 150, 100, 200, 10, "red.png")
RocketRight = Player(window_width - 100, window_heigh/2 - 150, 100, 200, 10, "blue.png")
Ball = GameSprite(window_width/2, window_heigh/2, 50, 50, 1, "ball.png")

score1 = 0
score2 = 0

speed_x = 8
speed_y = 8

finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False

    if finish != True:
        window.blit(background, (0, 0))
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y

        score1_text = font1.render(str(score2), True, (255, 255, 255))
        score2_text = font1.render(str(score1), True, (255, 255, 255))

        window.blit(score2_text, (527, 17))
        window.blit(score1_text, (743, 17))

        if Ball.rect.y > window_heigh - 50 or Ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(RocketLeft, Ball) or sprite.collide_rect(RocketRight, Ball):
            speed_x *= -1

        if Ball.rect.x < 0:
            score2 += 1
            finish = True

        if Ball.rect.x > window_width:
            score1 += 1
            finish = True

        RocketLeft.reset()
        RocketRight.reset()
        Ball.reset()
        RocketLeft.UpdateLeft()
        RocketRight.UpdateRight()

    else:
        finish = False
        Ball.rect.x = 200
        Ball.rect.y = 200
        # Сбрасываем скорость мяча
        speed_x = 8
        speed_y = 8

    display.update()
    clock.tick(FPS)
