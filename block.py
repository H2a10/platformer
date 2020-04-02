from base import *
class Block(Base):
    def __init__(self,x,y,image=0):
        #images is a integer to be looked up in IMAGE or surface
        super().__init__(x,y,image)
        self.update()
    def update(self):
        if isinstance(self.image,int):
            w.blit(IMAGE[self.image],map_coords((self.x,self.y)))
        else:
            w.blit(self.image,map_coords((self.x,self.y)))
        
IMAGE=[None,"1.png","2.png","3.png","4.png"]
for x in range(len(IMAGE)):
    if IMAGE[x]:
        IMAGE[x]=load_image(IMAGE[x])
s=p.Surface((16,16))
s.fill(BK)
IMAGE[0]=s
del s
IMAGE=tuple(IMAGE)
    
