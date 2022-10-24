#!/usr/bin/env python
# coding: utf-8

# In[5]:


class person:
    
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        
    def getname(self):
        return self.name
    
    def setname(self, newname):
        self.name = newname
        
    def getadress(self):
        return self.adress
    
    def setadress(self, newadress):
        self.adress = newadress
        
    def getdetails(self):
        print( self.getname() , self.getadress())
        


class student(person):
    
    def __init__(self, name, adress, program, year, fee):
        self.program = program
        self.year = year
        self.fee = fee        
        super().__init__(name, adress)
        
    def getprogram(self):
        return self.program
    
    def setprogram(self, newprogram):
        self.program = program
        
    def getyear(self):
        return self.year
        
    def setyear(self, newyear):
        self.year = newyear
        
    def getfee(self):
        return self.fee
    
    def setfee(self, newfee):
        self.fee= newfee
        
    def getdetailsstudent(self):
        print(super().getdetails(), self.getprogram(), self.getfee(), self.getyear())
        

    
class staff(person):
    
    def __init__(self, name, adress, school, pay):
        super().__init__(name, adress)
        self.school = school
        self.pay = pay

    def getschool(self):
        return self.school
    
    def setschool(self, newschool):
        self.school = newschool
        
    def getpay(self):
        return self.pay
    
    def setpay(self, newpay):
        self.pay = newpay
        
        
    def getdetailsstaff(self):
        print(super().getdetails(), self.getschool(), self.getpay())
        
        
mine1= staff('anushey', 'istanbul', 'AI', '2')
mine1.getdetailsstaff()
mine1.setpay('3')
mine1.getdetailsstaff()
        

        
        

        


# In[ ]:




