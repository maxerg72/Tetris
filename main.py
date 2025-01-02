import pygame as pg
import random as rd
import tetrominos as tm

#Setup and game initialization
pg.init()
screen_width = 250
screen_height = 500
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
running = True
background_color = (255, 14, 56)


# Game loop
while running:
    screen.fill((background_color))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                print("Left")

            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                print("Right")

            elif event.key == pg.K_UP or event.key == pg.K_w:
                print("Up")

            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                print("Down")

            elif event.key == pg.K_SPACE:
                print("Space")

            elif event.key == pg.K_ESCAPE:
                print("Game Ended")
                running = False


    # RENDER YOUR GAME HERE
    clock.tick(60)  #Game FPS

pg.quit()