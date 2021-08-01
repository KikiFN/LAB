import numpy as np

a=1
x0=5
L=10
J=101
cf=0.5

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

#1D
v=1

selected_entries_1D = {
    60:3,
    100:5,
    160:8,
    200:10,
    300:15,
    400:20
}



#VECTORS

distance = np.arange(0,20+deltat,deltat)