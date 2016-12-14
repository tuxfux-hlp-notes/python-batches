
# coding: utf-8

# In[ ]:

# Recursion/Looping
# other programming languages:for,foreach,do..while,while..do,until
# python: for,while
# for - finite loop
# while - infinite loop - conditions


# In[1]:

# for work on sequences
my_string="python"
for value in my_string:
    print value


# In[2]:

# ('linux','python','mysql','django') - tuple
# ['linux','python','mysql','django'] - list

for value in ('linux','python','mysql','django'):
    print value


# In[4]:

print help(range)


# In[22]:

print range(5)
print range(1,5) # 1 is start and 5 is end.
# for(i=1;i<10,i+2)
print range(1,10,2)
print range(1,10)
print range(1,10,1)
print range(1,2)
print range(-4,-1)
print range(10,1,-1)


# In[8]:

for value in range(1,11):
    print value


# In[9]:

m = iter(range(1,6))


# In[10]:

print m


# In[11]:

m.next()


# In[12]:

m.next()


# In[13]:

m.next()


# In[14]:

m.next()


# In[15]:

m.next()


# In[16]:

m.next()


# In[ ]:

# iterator vs generator

