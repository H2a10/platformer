import pygame,math,os
from pygame.locals import *
p=pygame
#CONSTANTS
BLOCK=16
NX=32
NY=16
WIDTH=BLOCK*NX
HEIGHT=BLOCK*NY
BLACK=(0,0,0)
WHITE=(255,255,255)
BK=BLACK
pupdate=p.display.update


p.init()
class Base(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.x=x
        self.y=y
        self.image=image
    def update(self):
        actw.blit(self.image,map_coords((self.x,self.y)))
class MoveSteady(Base):
    def __init__(self,x,y,image,angle,speed):
        #angle in degrees
        super().__init__(x,y,angle)
        self.rect=self.image.get_rect()
        self.speed=abs(speed)
        self.angle=math.radians(angle)
        self.v=p.Vector2((math.cos(self.angle)*self.speed),(math.sin(self.angle)*self.speed))
    def update(self):
        self.rect.pos=tuple(self.v)
        super().update()
w=p.display.set_mode((WIDTH,HEIGHT),0,32)
actw=w
w.fill(BK)
#global functions
def load_image(file):
    """ loads an image, prepares it for play
    """
    file = os.path.join(os.path.dirname(__file__),"recs", "images", file)
    try:
        surface = p.image.load(file)
    except p.error:
        raise SystemExit('Could not load image "%s" %s' % (file, p.get_error()))
    return surface.convert()

def map_coords(xy):
	return xy[0]*16,xy[1]*16
solidb=p.sprite.Group()
def alltype(iterable):
    t=type(iterable[0])
    for x in iterable:
        if not isinstance(x,t):
            return False
    return True
        
