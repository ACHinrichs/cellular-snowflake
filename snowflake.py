import cellular
import numpy as np
from matplotlib import colors
import random

class SnowRuler(cellular.Ruler):
    sizeX = 500
    sizeY = 500
    initialSpawnChance = 0.1
    
    def __init__(self):
        self.cmap = colors.ListedColormap(['black', 'xkcd:ice blue',])

    def move(self, x , y, dirX, dirY,field=None,newField=None):
        if(not (0<=x<self.sizeX)) or not( (0<=y<self.sizeY)):
            return newField
        
        if not (field[x][y] == 1):
            return newField

        field[x][y] = 0


        newX = (x + dirX + self.sizeX)%self.sizeX
        newY = (y + dirY + self.sizeY)%self.sizeY
            
        newField[newX][newY] = 1

        self.move((x-1+self.sizeX)%self.sizeX, y, dirX, dirY, field, newField)
        self.move((x+1)%self.sizeX           , y, dirX, dirY, field, newField)
        self.move(x, (y+1)%self.sizeY           , dirX, dirY, field, newField)
        self.move(x, (y-1+self.sizeY)%self.sizeY, dirX, dirY, field, newField)
        return (field,newField)
        
    def rule(self,x,y,field=None,newField=None):
        if(field[x][y] == 1):
            direction = random.randint(1,4)
            if direction == 1:
                field,newField=self.move(x,y, 0,-1,field,newField)
            elif direction == 2:
                field,newField=self.move(x,y, 0, 1,field,newField)
            elif direction == 3:
                field,newField=self.move(x,y,-1, 0,field,newField)
            elif direction == 4:
                field,newField=self.move(x,y, 1, 0,field,newField)
        return (field,newField)
    
    def initField(self):
        initialField = np.zeros((self.sizeX,self.sizeY))
        print(str(initialField))
        for x,row in enumerate(initialField):
            for y,cell in enumerate(row):
                if random.random() < self.initialSpawnChance:
                    initialField[x][y]=1
        return initialField

sim = cellular.Automaton(SnowRuler())
sim.delay=0.1
sim.start()
