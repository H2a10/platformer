from base import *
from itertools import cycle
class Block(Base):
    def __init__(self,x,y,image=0,solid=None):
        #images is a integer to be looked up in IMAGE or surface
        super().__init__(x,y,image)
        self.solid=bool(solid)
        self.update()
        if self.solid:
            solidb.add(self)
    def update(self):
        if isinstance(self.image,int):
            actw.blit(IMAGE[self.image],map_coords((self.x,self.y)))
        else:
            actw.blit(self.image,map_coords((self.x,self.y)))
class BlockMul(Block):
    def __init__(self,x,y,images=[0],solid=None):
        self.next=False
        super().__init__(x,y,images[0])
        assert alltype(images)
        self.images=cycle(images)
        if solid:
            self.solid=solid
    def update(self):
        if self.next:
            self.image=next(self.images)
            self.next=False
        super().update()
IMAGE=[None]
for x in range(1,79):
    IMAGE.append(f"{x}.png")
for x in range(len(IMAGE)):
    if IMAGE[x]:
        IMAGE[x]=load_image(IMAGE[x])
s=p.Surface((BLOCK,BLOCK))
s.fill(BK)
IMAGE[0]=s
del s
IMAGE=tuple(IMAGE)

