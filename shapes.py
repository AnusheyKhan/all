#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import abstractmethod


class shape():

    def __init__(self, color, filled):
        self. color = color
        self.filled = filled


    def getcolor(self):
        return self.color

    def setcolor(self, newcolor):
        self.color = newcolor

    def getfilled(self):
        return self.filled

    def setfilled(self, newfilled):
        self.filled = newfilled

    @abstractmethod
    def getarea(self):
        pass

    @abstractmethod
    def getperimeter(self):
        pass
class circle(shape):

    def __init__(self, radius, color, filled):
        self.radius = radius
        super().__init__(color, filled)

    def getarea(self):
        print(3.142*self.radius*self.radius)

    def getdetails(self):
        print(super().getfilled , super().getcolor(), self.getarea())



circle1 = circle(3, 'red', True)

circle1.getdetails()



