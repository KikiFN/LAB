a=1
x0=5
L=10
J=101
cf=0.5

u = []
un,un2,norme = [],[],[]
err=[]

deltax= L/(J-1)
deltat= (deltax * cf)/a