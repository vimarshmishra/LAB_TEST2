#!/usr/bin/env python
# coding: utf-8

# In[27]:


strings=input("Enter array of strings seperated by space ")
strings=strings.split(" ")
def compare(j,string,size):
    print(size)
    for i in range(0,size):
        if(j[i]!=string[i]):
            return False
    return true
def reverse_t(string,strings,i):
    x=string
    size=len(strings)
    for j in range(0,size):
        print(len(string),len(strings[j]))
        if(len(string)==len(strings[j]) and i!=j):
            k=strings[j]
            sorted(k)
            sorted(string)
            print(k,string)
            if(compare(k,string,len(k))): 
                print(compare(k,string,len(k)))
                return x[::-1]
        else:
            return x
        
print(strings)
strings=strings[::-1]
size=len(strings)
for i in range(0,size):
     strings[i]= reverse_t(strings[i],strings,i)

       
print(strings)


# In[9]:





# In[ ]:




