#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 10:21:08 2019

@author: allen
"""

#Class and attributes
class Simple():
    pass

myObject = Simple() #Oject
type(myObject)


#====== Class Oject attributes======== 
class Person():
    
   
    def __init__(self,name,age):
        self.name =name
        self.age = age
        
P1 = Person("Allen Muhani",20)        
type(P1)        


print(str(P1.name) + str(P1.age))


class Person():
    
    eyes = "blue"
    
    def __init__(self,name,age):
        self.name =name
        self.age = age
P1 = Person("Allen Muhani",20)         
print("name : "+str(P1.name)+ "   age : "+str(P1.age)+ "  eye pigment : "+str(P1.eyes))



#  ================ methods ==================================

class Person():
    def __init__(self,name,age):
        
        self.age = age
        self.name = name 
    def myFunction(self,number):
        print("I am {} , age {} and my number is {}".format(self.name,self.age,number))


P1 = Person("Muhani Allen",20)

print(P1.age)
print(P1.name)

P1.myFunction(791725651)



class Circle:
    pi = 3.14231
    
    def __init__(self,radius):
        self.radius = radius
        self.area = self.pi * radius * radius
        self.circumference = 2*self.pi*self.radius
        
    def Circumference(self):
        circumference = 2*self.pi*self.radius
        return circumference
    
    def outPut(self):
        print("Radius : {}     Circumference : {}    Area : {}".format(self.radius,self.circumference,self.area))
    

C1 =Circle(28)
C1.outPut()    

### ================================inheritance ==============================
class Sports():
    def __init__(self):
        print("Enjoy the game")
    def health(self):
        print("I am healthy")
    def excitement(self):
        print("I am exciting")
        
mySport = Sports()
mySport.excitement()
mySport.health()

class Football(Sports):
    def __init__(self):
        Sports.__init__(self)
        print("I am football")


myFootball = Football()
myFootball.excitement()
myFootball.health()      
        



