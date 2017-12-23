import cellular
import numpy as np
from matplotlib import colors
import random

class SnowRuler(cellular.Ruler):
    sizeX = 150
    sizeY = 150
    initialSpawnChance = 0.05
    runningSpawnChance = 0.002
    cmap = colors.ListedColormap(['black', 'xkcd:ice blue',])
    
    def __init__(self):
        pass

    def move(self, x , y, dirX, dirY,field=None,newField=None):
        if(not (0<=x<self.sizeX)) or not( (0<=y<self.sizeY)):
            return (field,newField)
        
        if not (field[x][y] == 1):
            return (field,newField)

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
        if( field[x][y] == 1):
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

class NonMovingSnowRuler(SnowRuler):

    cmap = colors.ListedColormap(['black','white', 'xkcd:ice blue','blue'])
    def move(self, x , y, dirX, dirY,field=None,newField=None):
        if(not (0<=x<self.sizeX)) or not( (0<=y<self.sizeY)):
            return newField

        if field[x][y]==2:
            newField[x][y]==2
        if not (field[x][y] == 1):
            return (newField,field)

        #field[x][y] = 0

        

        sticking = False
        for dX,dY in [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]:
            if(field[(x+dX+self.sizeX)%self.sizeX][(y+dY+self.sizeY)%self.sizeY]>=2):
                sticking=True
        newX = (x+dirX+self.sizeX)%self.sizeX
        newY = (y+dirY+self.sizeY)%self.sizeY
        
        if(sticking or
           field[newX][newY]>=2):
           newField[x][y]=2
        elif(newField[newX][newY]==0):
           newField[newX][newY] = 1
        return (field,newField)
    
    def rule(self,x,y,field=None,newField=None):
        if(field[x][y]==2):
            newField[x][y]=2
        elif(field[x][y]==3):
            newField[x][y]=3
        else:
            field,newField = super(NonMovingSnowRuler,self).rule(x,y,field,newField)
        if (newField[x][y]==0 and
            (not (self.sizeX/4 < x < 3*self.sizeX/4 and
                  self.sizeY/4 < y < 3*self.sizeY/4)) and
            random.random()<self.runningSpawnChance):
            newField[x][y]=1
        return (field,newField)

    def initField(self):
        initialField = super(NonMovingSnowRuler,self).initField()
        initialField[self.sizeX // 2][self.sizeY // 2]=3
        return initialField

sim = cellular.Automaton(NonMovingSnowRuler())
sim.delay=0
sim.start()
