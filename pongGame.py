import pygame

def main():

    pygame.display.set_caption("Pong")
    # creating a surface

    WIDTH = 800
    HEIGHT = 400
    BORDER = 15
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    screen.fill((0,0,0))
    # double buffering: stage all changes anf update them all at once
    # avoid flickering
    pygame.display.update()


    #draw walls as rectangles
    wcolor = pygame.Color("white")
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(WIDTH,BORDER)))
    #left wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,0),(BORDER,HEIGHT)))
    #bottom wall
    pygame.draw.rect(screen,wcolor,pygame.Rect((0,HEIGHT-BORDER),(WIDTH,BORDER)))

    pygame.display.update()

    #define a variable to control main loop
    running = True

    # main loop
    while running:
        # event handeling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type quit
            if event.type == pygame.QUIT:
                # change value to false to exit main loop
                running = False
                
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()