#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('1. Hello World in Python:\n')
print('hello world')


# In[2]:


print('\n2. String Operations in Python:\n')
a='compare Python with Java'
print(a.split())


# In[3]:


print('3. Control Flow in Python:\n')
#if
condiction=10
if condiction >10:
    print('>10')
elif condiction ==10:
    print('=10')
else:
    print('<10')
#while
while condiction>1:
    print(condiction)
    condiction=condiction -1
print('while result end\n')
#switch
def f(x):
    return{
          1:1,
          2:2,
 }[x]
print(f(condiction))
print('switch result end\n')
#for
for x in range(1,10):
    print(x)


# In[7]:


print('\n4. Class&Inheritance in Python:')
class Animal():
    def __init__(self,name):
        self.name=name
    def Saysomething(self):
        print('I am'+self.name)
class Dog(Animal):
    def Saysomething(self):
        print('I am '+self.name+',and I can bark')
dog=Dog('Chiwawa')
dog.Saysomething()


# In[10]:


print('\n5.File I/O in Python')
text='This is my first test\n'
myFile=open('myfile.txt','w')
myFile.write(text)
myFile=open('myfile.txt','r')
print(myFile.read())
myFile.close()


# In[ ]:


print('\n6. NULL in Python:')
special=None


# In[8]:


print('\n7.Collections in Python')
aList=[]
aList.append('a')
aList.append('b')
aList.append('c')
print(aList)


# In[12]:


print('\n8.Numbers in Python')
num=100
num=int(100)
f=1.01
f=float(1.01)
special=None


# In[21]:


print('\n9.Tuple in Python')
aTuple=()
#aTuple=(5)
aTuple=(5,)
print(aTuple)
print(aTuple[0])


# In[22]:


print('\n10.Set in Python')
aSet=set()
aSet=set('one')
aSet=set(['one','two','three'])
for v in aSet:
    print('aSet:'+v)  
bSet=set(['three','four','five'])
cSet=aSet|bSet
print('aSet OR bSet:')
print(cSet)
dSet=aSet&bSet
print('aSet AND bSedSet')
print(dSet)
eSet=aSet.difference(bSet)
print('aSet difference bSet')
print(eSet)
bSet.add('six')
print('bSet add six:')
print(bSet)


# In[23]:


print('\n11.Dictionaries in Python\n')
phoneBook={}
phoneBook={'Mike':'555-1111',
           'Lucy':'555-2222',
           'Jack':'555-3333'}
for key in phoneBook:
    print(key,phoneBook[key])
phoneBook['Mary']='555-6666'
del phoneBook['Mike']
count=len(phoneBook)
phoneBook['Susan']=(1,2,3,4)
print(phoneBook.keys())
print(phoneBook['Susan'])
phoneBook.clear()
print(phoneBook)
    


# In[ ]:




