#!/usr/bin/env python
# coding: utf-8

# # Encapsulation

# # Encapsultion: Means restrict the access to the variable and methods

# # Private Methods:

# In[5]:


class car:
    def __init__(self):
        self.__updatesoftware()  #here updatesoftware is private method
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")
redcar=car()    # when object created it will automatically call init method
redcar.drive()


# # Private Variable:

# # Private variable can modify only inside class methods we cant modify outside private variable outside the class

# In[6]:


class car:
    __maxspeed=0   ##private variable
    __name=''
    def  __init__(self):
        self.__maxspeed=200      #assign value
        self.__name="supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed): #modify variable
        self.__maxspeed=speed
        print(self.__maxspeed)
redcar=car()
redcar.drive()
redcar.setspeed(100)


# In[ ]:




