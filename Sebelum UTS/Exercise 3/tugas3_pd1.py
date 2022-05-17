from solver import *
import matplotlib.pyplot as plt
import math

def pendulumfunc(g, l, a):
  return -(g/l) * math.sin(a)

parameter = {
  'g' : 9.8,
  'y0' : 1,
  't0' : 0,
  't_akhir' : 4,
  'h' : 0.001,
  'dy0' : 0.5 * 3.14
}


t, res = cauchy_euler(parameter, pendulumfunc)

plt.plot(t,res)
plt.show()