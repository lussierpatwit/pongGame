from paddle import Paddle
from ball import Ball
import pygame
import random
from collections import namedtuple

def main():

    pygame.display.set_caption("Pong")
    # creating a surface

    WIDTH = 800
    HEIGHT = 400
    BORDER = 20
    VELOCITY = 5
    FPS = 60

    MyConstants = namedtuple("MyConstants",["WIDTH","HEIGHT","BORDER","VELOCITY","FPS"])

    CONSTANTS = MyConstants(WIDTH,HEIGHT,BORDER,VELOCITY,FPS)
    # print(CONSTANTS.BORDER)
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    screen.fill((0,0,0))
    # double buffering: stage all changes anf update them all at once
    # avoid flickering
    pygame.display.update()


    #draw walls as rectangles
    fgcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")
    pygame.draw.rect(screen,fgcolor,pygame.Rect((0,0),(WIDTH,BORDER)))
    #left wall
    pygame.draw.rect(screen,fgcolor,pygame.Rect((0,0),(BORDER,HEIGHT)))
    #bottom wall
    pygame.draw.rect(screen,fgcolor,pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    if(random.randint(0,1) == 0):
        vy0 = 20
    else:
        vy0 = -20
    # TODO: +/- 45 degrees
    b0 = Ball(x0,y0, vx0,vy0,screen,fgcolor,bgcolor,CONSTANTS)
    b0.show(fgcolor)


    pygame.display.update()

    #define a variable to control main loop
    running = True
    clock = pygame.time.Clock()
    # main loop
    while running:
        # event handeling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type quit
            if event.type == pygame.QUIT:
                # change value to false to exit main loop
                running = False
                # Ball
            pygame.display.update()
            clock.tick(FPS)
            b0.update()

                
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()