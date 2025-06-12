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

bullets = sprite.Group()


font.init()
font1 = font.Font(None, 80)
win = font1.render("YOU WIN!", True, (255,255,255))
lose = font1.render("You lose :(", True, (180, 0, 0))
font2 = font.Font(None, 36)

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

    def fire(self):
        bullet = Bullet("куля.png", self.rect.centerx, self.rect.top, 20, 25, 15)
        bullets.add(bullet)

player = Player("хмарка.png", WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] - 125, 250, 85, 5)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > WINDOW_SIZE[1]:
            self.rect.x = randint(80, WINDOW_SIZE[0] - 80)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

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
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if not finish:
        window.blit(background, (0, 0))
        player.update()
        player.draw()
        bullets.update()
        bullets.draw(window)
        monsters.update()
        monsters.draw(window)

        if sprite.spritecollide(player, monsters, False):
            sprite.spritecollide(player, monsters, True)
            life -= 1
        collides = sprite.groupcollide(bullets, monsters, True, True)
        for c in collides:
            score += 1
            monster = Enemy("противник.png", randint(80, WINDOW_SIZE[0] - 80), -40, 75, 75, randint(1,3))
            monsters.add(monster)

        text_win = font2.render("Рахунок: " + str(score), 1, (255, 255, 255))
        window.blit(text_win, (10, 20))

        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (150, 150, 0)
        if life == 1:
            life_color = (150, 0, 0)

        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))

        if score >= goal:
            print("Ти виграв!")
            finish =  True
            window.blit(win, ((WINDOW_SIZE[0] - win.get_width()) / 2, WINDOW_SIZE[1] / 2))
        if life <= 0:
            print("Ти програв:(")
            finish =  True
            window.blit(lose, ((WINDOW_SIZE[0] - win.get_width()) / 2, WINDOW_SIZE[1] / 2))
        if lost >= max_lost:
            print("Ти програв:(")
            finish =  True
            window.blit(lose, ((WINDOW_SIZE[0] - win.get_width()) / 2, WINDOW_SIZE[1] / 2))

    clock.tick(FPS)
    display.update()