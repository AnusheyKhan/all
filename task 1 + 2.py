#!/usr/bin/env python
# coding: utf-8

#  Write a class called Circle, which has a instance variable, radius. Write methods to 
# calculate the area of the circle and modify the radius

# In[2]:


import math

class Circle:
    
    def __init__(self):
        self.radius=0
   
    def __init__(self,radius):
        self.radius=radius
  
    def area(self):
        return math.pi*self.radius*self.radius


class Cyclinder(Circle):
   
    def __init__(self):
        super().__init__()
        self.height=0
  
    def __init__(self, radius,height):
        super().__init__(radius)
        self.height=height

    def surfaceArea(self):
        result=2*math.pi*getattr(self,"radius")*self.height + 2*super().area()
        return result

    def Volume(self):
        result = super().area()*self.height
        return result

obj=Cyclinder(2,5)
print("The surface area is "+str(obj.surfaceArea()))
print("The Volume is "+str(obj.Volume()))
    


# In[ ]:





# In[ ]:




