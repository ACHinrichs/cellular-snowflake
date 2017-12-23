# cellular.py
#
# Date: 20171223
# Author: ACHinrichs
#
# Description: Provides the basic functionality for a cellular automaton in Python
from abc import ABC, abstractmethod, abstractproperty
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import time

class Ruler(ABC):
    @abstractmethod
    def __init__(self):
        self.cmap = colors.ListedColormap(['white', 'black',])
        pass
    
    @abstractmethod
    def rule(self,x,y,field,newfield):
        newField=field
    
    @abstractmethod
    def initField(self):
        return array([])


# The cellualar automaton itself
class Automaton:
    delay = 0.25 
    def __init__(self, ruler):
        self.ruler = ruler
        self.field=ruler.initField()
        self.fig = plt.figure()

        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)
        self.grid = plt.imshow(self.field,
                               interpolation='nearest',
                               cmap=self.ruler.cmap)
        plt.ion() 
        plt.show()
        self.paint(self.field)
        
    def paint(self,field):
        self.grid.set_data(field)
        self.fig.canvas.draw()
        
    def start(self):
        running = True
        while(running):
            time.sleep(self.delay)
            newField= np.zeros(self.field.shape)
            for x,row in enumerate(self.field):
                for y,cell in enumerate(row):
                    self.field,newField=self.ruler.rule(x,y,self.field, newField)
            self.field=newField
            self.paint(self.field)
