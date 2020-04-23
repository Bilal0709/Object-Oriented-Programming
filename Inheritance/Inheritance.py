#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Parent:
    def __init__(self,fname,fage):
        self.name=fname
        self.age=fage
        
    def view(self):
        print(self.name,self.age)
class child(Parent):
    def __init__(self,fname,fage):
        Parent.__init__(self,fname,fage)
        self.lastname="Ahmad"
    def view(self):
        print(self.name,self.lastname,self.age)
obj=child("Ali",25)
obj.view()


# In[ ]:




