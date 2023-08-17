# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
"""
x = 2.
n = 10
func = np.zeros(n)
# func = np.zeros(n, )
#type(func)
func[0] = x
#func[1] = 1/2((x/(func[0]))+func[0])
#print(func[0])
#print(func[1])
def update(f,x):
    f = (x/f + f)/2
    return f
#update(x, x)
#print(update(func[0], x))
for i in range(1,n):
    func[i] = update(func[i+1],x)
    print(func[i])
    
k = np.arange(0,n,1)
plt.scatter(k,func)
a  = plt.axhline( y = np.sqrt(2), color='r')
print(a)"""
#y = (3*x + 5)
def distancia(x,y):
    np.sqrt(x**2 + y**2)
 