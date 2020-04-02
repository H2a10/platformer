from base import *
import json
class Level(p.Surface):
    def __init__(self,data):
        self.data=data
        super().__init__((0,0))
    def update(self):
        pass
        
        
def lvp(file):
    f=open(file)
    data=None
    json.load(data,f)
    
