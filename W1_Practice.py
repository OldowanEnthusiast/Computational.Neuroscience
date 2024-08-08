# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

#Q1
A = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])

#Q2
B = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
C = B[[0,2],1:]
C

#Q5,6,7
x=np.random.rand(100)
x[x>0.5]=1

#which one???
#(x>1)[:3]
#x[:3]>1
#(x>1).nonzero()[0][:3]
#x[x>1][:3]

#Q8
#What piece of code loads the file 'data.pickle', which contains a dict object, into the variable "data"? 
#You can assume that the directory containing 'data.pickle' is in your path (i.e., is accessible). 
#The end result should be that the variable data is a dict object.
import pickle
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

#Q9
#Suppose the dict called "data" has been set to {'a': 3, 'c': 9, 'b': 5}. 
#How do you set the value corresponding to the key 'b' to 100?
data['b'] = 100

#Q10
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5, step=0.05)
y = np.sin(x**2)
plt.plot(x,y)
plt.show()

#Q12
x = np.array([[1, 2, 3], [2, 3, 4]])
x *= 5
x -= 1
x[x > 10] = 0
x = x.T
print(x)

#Q13
#Which of the following pieces of code sets the value of y to True 
#if the value of x is either 2, 5, or 9, and to False otherwise?


#Q14
#What does this do: import pdb; pdb.set_trace()
#Interrupts execution and temporarily gives control to the user.
#Lets you debug