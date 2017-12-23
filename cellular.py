# cellular.py
#
# Date: 20171223
# Author: ACHinrichs
#
# Description: Provides the basic functionality for a cellular automaton in Python
from abc import ABC, abstractmethod, abstractproperty
import numpy as np
import matplotlib.pyplot as plt
import time

class Rule(ABC):
    @abstractmethod
    def __init__(self):
        self.cmap = colors.ListedColormap(['white', 'blue',])
        pass
    
    @abstractmethod
    def rule(x,y,field,newfield):
        pass
    
    @abstractmethod
    def initField():
        pass


# The cellualar automaton itself
class Cellular:
    def __init__(self, rule):
        self.ruler = rule
        self.field=ruler.initField()
        paint(field)
        self.fig = plt.figure()

        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)
        self.grid = plt.imshow(field,
                               interpolation='nearest',
                               cmap=self.ruler.cmap)
        plt.show()
        
    def paint(field):
        grid.set_data(new_state)
        
    def start(self):
        running = true
        while(running):
            time.sleep(1)
            newFieled= np.zeros(field.shape)
            for x,y in numpy.nditer(field):
                ruler.rule(x,y,field,newField)
            field=newField
            paint(field)
