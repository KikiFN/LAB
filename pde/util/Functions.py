import numpy as np 
from numpy import linalg as LA
import util.parameters as pr
import matplotlib.pyplot as plt
import util.settings as stg
import os

class Functions:

    def __init__(self):
        
        def _indexes():
            a= np.asarray([i for i in range(0,self.LEN)])
            b= np.roll(a,1)
            c= np.roll(a,-1)
            return a,b,c
        
        self.deltax = pr.L/(pr.J-1)
        self.deltat = (self.deltax * pr.cf) / pr.a

        self.x_val = np.arange(0,pr.L,self.deltax)
        
        self.gauss = np.exp(-np.power(self.x_val-pr.x0,2))
    
        self.LEN = len(self.x_val)
        self.j,self.jmin,self.jmax = _indexes()
        
        self.coefficient = (pr.a*self.deltat)/(2*self.deltax)
            
    def get_gaussian(self):
        return self.gauss
    
    def ftcs(self,v=None):
        if v is None: v= self.get_gaussian()
        curve = [ v[a] - (self.coefficient)*(v[b]-v[c]) for a,b,c in zip(self.j,self.jmax,self.jmin)]
        
        return curve

    def get_norm(v,self):
        return LA.norm(v)/np.sqrt(pr.J)
    
    def cartesian_plot(self,*args):
        x,y = args
        plt.plot(x,y)
        
    def pre_plot(self,n):
        fig=plt.figure(n)


    def plot(self,data):
        plt.plot(*data)


    def post_plot(self,*args):
        xlb,ylb,title,figname= args
        plt.xlabel(xlb)
        plt.ylabel(ylb)
        plt.title(title)
        plt.savefig(os.path.join(stg.DATA_PATH, figname), dpi=100)