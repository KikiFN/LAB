import numpy as np

a=1
x0=5
L=10
J=301
cf=0.5

deltax= L/(J-1)
deltat= (deltax * cf)/a

selected_entries = {
    300:5,
    600:10,
    900:15,
    1200:20
}

error_entries = {
    600:10,
    1200:20
}


#VECTORS

distance = np.arange(0,20+deltat,deltat)