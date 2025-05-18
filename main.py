from pygame import *

WINDOW_SIZE = (1280,720)
window = display.set_mode(WINDOW_SIZE)
background = transform.scale(image.load("фон.jpg"), WINDOW_SIZE)
display.set_caption("Збий ворогів!")

clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    window.blit(background, (0, 0))
    clock.tick(FPS)
    display.update()