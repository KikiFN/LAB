import numpy as np

#common

a=1
x0=5
L=10
J=101
cf=0.5

#1D
v=1

deltax= L/(J-1)
deltat= (deltax * cf)/a

selected_entries = {
    100:5,
    200:10,
    300:15,
    400:20
}

error_entries = {
    200:10,
    400:20
}

#VECTORS

distance = np.arange(0,20+deltat,deltat)