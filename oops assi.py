#!/usr/bin/env python
# coding: utf-8

# In[3]:


class sqr:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def answer(self):
        result=self.x**self.n
        return(result)
a=sqr(10,2)
result=a.answer()
print(result)


# In[ ]:




