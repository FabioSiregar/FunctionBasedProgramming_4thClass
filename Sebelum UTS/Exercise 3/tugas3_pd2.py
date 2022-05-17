import matplotlib.pyplot as plt
from solver import *
import math

def pd2(y, dy, x):
    return -y - dy - (math.sin(x) ** 2)

parameter1 ={
    't0' : 0,
    't_akhir' : 50,
    'h' : 0.05,
    'y0' : 1,
    'dy0' : -9/2
}

x, y = cauchy_euler(parameter1, pd2)

plt.plot(x,y)
plt.show()