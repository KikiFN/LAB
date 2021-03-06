import numpy as np 
from numpy import linalg as LA
import util.parameters101 as pr
import matplotlib.pyplot as plt
import util.settings as stg
import os
import logging

logger = logging.getLogger(__name__)

class Functions:

    def __init__(self):
        
        def _indexes():
            a= np.asarray([i for i in range(0,self.LEN)])
            b= np.roll(a,1)
            c= np.roll(a,-1)
            return a,b,c

        self.x_val = np.arange(0,pr.L,pr.deltax)
        self.t_val = np.arange(0,20+pr.deltat,pr.deltat) 
        self.LEN = len(self.x_val)
        self.j,self.jmin,self.jmax = _indexes()
        
        self.coefficient = (pr.a*pr.deltat)/(2*pr.deltax)
        self.coeff1D_LP = (((pr.v**2)*(pr.deltat**2))/(pr.deltax**2))
        self.coeff1D_LW = (np.power(pr.a,2)*np.power(pr.deltat,2)/(2*np.power(pr.deltax,2)))
        

    def _get_norm(self,v):
        return LA.norm(v)/np.sqrt(pr.J)
    
    def _get_err(self,v):
        return self._get_norm(v - self.get_gaussian())
    
    def add_to_array(self,opr_type,un,arr):
        if opr_type == "norm": vec = self._get_norm(un)
        if opr_type == "err": vec = self._get_err(un)
        arr = np.append(arr,vec)
        return arr
    
    def cartesian_plot(self,*args):
        x,y = args
        plt.plot(x,y)

    def ftcs(self,v=None):
        if v is None: v= self.get_gaussian()
        curve = [ v[a] - (self.coefficient)*(v[b]-v[c]) for a,b,c in zip(self.j,self.jmax,self.jmin)]
        return np.asarray(curve)
    
    def get_gaussian(self,a=None,b=None,ctype=None):
        if a == None: a= self.x_val
        if b == None: b= pr.x0
        if ctype == "1D": return (1/2)*(np.exp(-np.power(a-(b-pr.deltat),2))) + (1/2)*(np.exp(-np.power(a-(b+pr.deltat),2)))
        else: return np.exp(-np.power(a-(b),2))
    
    def initialize_arrays(self,n):
        arr_list = []
        for i in range(n):
            x = np.empty(0)
            arr_list.append(x)
        return arr_list
    
    def laxfried(self,v=None):
        if v is None: v= self.get_gaussian()
        curve = [ (0.5*(v[a]+v[b])) - ((self.coefficient)*(v[a]-v[b])) for a,b in zip(self.jmax,self.jmin)]
        return np.asarray(curve)
    
    def laxwendroff(self,v=None,ctype=None):
        if v is None: v= self.get_gaussian()
        second_coeff = (np.power(pr.a,2)*np.power(pr.deltat,2))/(2*np.power(pr.deltax,2))
        curve = [ v[a] - ((self.coefficient)*(v[b]-v[c])) + (second_coeff)*(v[b]-(2*v[a])+v[c]) for a,b,c in zip(self.j,self.jmax,self.jmin)]
        return np.asarray(curve)
    
    def leapfrog(self,v,w,ctype=None): #v u0 w u
        if ctype == "1D":
            curve = [ (2*w[a] - v[a] + self.coeff1D_LP*(w[b] - 2*w[a] + w[c])) for a,b,c in zip(self.j,self.jmax,self.jmin)]
        else:
            curve = [ (v[a] - ((2*self.coefficient)*(w[b]-w[c]))) for a,b,c in zip(self.j,self.jmax,self.jmin)]
        return np.asarray(curve)

    def pre_plot(self,n):
        fig=plt.figure(n)
        logger.info("Pre-plotting figure number {}".format(str(n))) 
        
    def plot(self,args):
        data,label= args
        if label == "": plt.plot(*data)
        else:
            plt.plot(*data,label=label)
            plt.legend(loc=0)
        logger.info("Plotting function labeled {}".format(str(label))) 

    def post_plot(self,*args):
        appname,xlb,ylb,title,figname= args
        figname += "_{}".format(str(pr.J))
        plt.xlabel(xlb)
        plt.ylabel(ylb)
        plt.title(title)
        name = appname + "_" + figname
        plt.savefig(os.path.join(stg.DATA_PATH, name), dpi=100)
        logger.info("Post-plotting and saving figure {}".format(str(name))) 
        plt.close()
        
    def step_fun(self,v=None):
        if v is None: v=self.x_val
        x = np.zeros(len(v))
        for i,num in enumerate(v):
            if (num >=4. and num <=6.): x[i]=1
        return x
    
    def wendroff_rs_100(self,a,t,b,X=None,Y=None):
        if t==0:
            r = -2*np.exp(-np.power(a-t-b,2))*(a-t-b)
            s = 0
        else:
            r = [ (X[a] + self.coefficient*(Y[b]-Y[c]) + self.coeff1D_LW*(X[b]-(2*X[a])+[X[c]])) for a,b,c in zip(self.j,self.jmax,self.jmin)]
            s = [ (Y[a] + self.coefficient*(X[b]-X[c]) + self.coeff1D_LW*(Y[b]-(2*Y[a])+[Y[c]])) for a,b,c in zip(self.j,self.jmax,self.jmin)]
            
        return r,s