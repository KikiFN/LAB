import numpy as np 
import util.parameters as pr

class Functions:

    def __init__(self):
        
        self.deltax = pr.L/(pr.J-1)
        self.deltat = (self.deltax * pr.cf) / pr.a
    
        self.x_val = np.arange(0,pr.L,self.deltax)
        
        self.gauss = np.exp(-np.power(self.x_val-pr.x0,2))
    
        self.LEN = len(self.x_val)
        
    def _indexes(self):
        a= [i for i in range(0,self.LEN)]
        b= np.roll(a,1)
        c= np.roll(a,-1)
        return a,b,c
    
    def testresult(self):
        j,jmin,jmax = self.indexes()
        g= self.gauss
        for a,b,c in zip(j,jmin,jmax):
            print(g[a],g[b],g[c])
            
    def ftcs(self):
        j,jmin,jmax = self.indexes()
        g = self.gauss
        coefficient = (self.a*self.deltat)/(2*self.deltax)
        print(coefficient)
        curve = [ g[a] - (coefficient)*(g[b]-g[c]) for a,b,c in zip(j,jmin,jmax)]
        return curve