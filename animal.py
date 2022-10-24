#!/usr/bin/env python
# coding: utf-8

# In[ ]:





class animal:

    def __init__(self, name):
        self.name = name


    def setanimalname (self, name):
        self.name = name

    def getanimalname(self):
        return self.name

    def getanimaldetails(self):
        print(self.getanimalname())



class mammal(animal):

    def __init__(self, animalname, mammalname):
        self.mammalname = mammalname
        super().__init__(animalname)

    def setmammalname (self, mammalname):
        self.mammalname = mammalname

    def getmammalname(self):
        return self.mammalname

    def getmammaldetails(self):
        print(self.getmammalname(), super().getanimaldetails())


class cat(mammal):

    def __init__(self, catname, mammalname , animalname):
        self.catname= catname

        super().__init__(mammalname, animalname)

    def setcatname (self, catname):
        self.catname = catname

    def getcatname(self):
        return self.catname

    def greetingforcat(self):
        print(self.getcatname(), "says meow")

    def getcatdetails(self):
        print(super().getmammaldetails(), self.getcatname())


class dog(mammal):

    def __init__(self, dogname, animalname, mammalname):
        self.dogname = dogname
        super().__init__(mammalname, animalname)

    def setname(self, dogname):
        self.dogname = dogname

    def getname(self):
        return self.dogname

    def greeting(self):
        print(self.getname(), "says woof")

    def getdetails(self):
        print(super().getdetails(), self.getname())


list = []
list.append("tony")
object = cat(list[0], 'cat', 'yes')
object.getcatdetails()
object.greetingforcat()






