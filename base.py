import pygame,math
from pygame.locals import *

#CONSTANTS
WIDTH=512
HEIGHT=256

class Base(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.x=x
        self.y=y
        self.image=image

class MoveSteady(Base):
    def __init__(self,x,y,image,angle,speed):
        #ngle in degrees
        super().__init__(x,y,angle)
        self.rect=self.image.get_rect()
        self.speed=abs(speed)
        self.angle=math.radians(angle)
        self.v=p.Vector2((math.cos(self.angle)*self.speed),(math.sin(self.angle)*self.speed))
    def update(self):
        self.rect.pos=tuple(self.v)
