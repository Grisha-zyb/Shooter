from pygame import *
from random import randint

WINDOW_SIZE = (1280,720)
window = display.set_mode(WINDOW_SIZE)
background = transform.scale(image.load("фон.jpg"), WINDOW_SIZE)
display.set_caption("Збий ворогів!")

clock = time.Clock()
FPS = 60

score = 0
goal = 15
lost = 0
max_lost = 5
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        
        if keys [K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys [K_d] and self.rect.x < WINDOW_SIZE[0] - self.rect.width:
            self.rect.x += self.speed

player = Player("хмарка.png", WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] - 125, 250, 85, 5)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > WINDOW_SIZE[1]:
            self.rect.x = randint(80, WINDOW_SIZE[0] - 80)
            self.rect.y = 0
            lost += 1

monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy("противник.png", randint(
        80, WINDOW_SIZE[0] - 80), -40, 75, 75, randint(1,3))
    monsters.add(monster)
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        player.update()
        player.draw()
        monsters.update()
        monsters.draw(window)
    clock.tick(FPS)
    display.update()