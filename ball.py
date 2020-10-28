import pygame
class Ball:
     # pass
    RADIUS = 10

    def __init__(self,x,y, vx,vy, screen, fgcolor,bgcolor, CONSTANTS):
        self.x = x
        self.y = y
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.vx = vx
        self.vy = vy
        self.CONSTANTS = CONSTANTS
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    def update(self):
        # print(self.x)
        # new position = old position + delta position(velocity)
        #TODO: 
        # check if collison (wall position)
            #  flip velocity
        if( self.x < (self.CONSTANTS.BORDER + self.RADIUS + 4)):
            # print("In if")
            self.vx = -self.vx
        if( self.y < (self.CONSTANTS.BORDER + self.RADIUS + 20) or self.y > (self.CONSTANTS.HEIGHT - self.RADIUS - 35)):
            self.vy = -self.vy

        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        self.show(self.fgcolor)
