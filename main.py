from pygame import *

WINDOW_SIZE = (1280,720)
window = display.set_mode(WINDOW_SIZE)
background = transform.scale(image.load("фон.jpg"), WINDOW_SIZE)
display.set_caption("Збий ворогів!")

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h)))
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

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    clock.tick(FPS)
    display.update()