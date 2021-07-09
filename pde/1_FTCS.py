from util.Functions import *
import util.parameters as pr
import numpy as np


fn = Functions()
u0 = fn.get_gaussian()
u =fn.ftcs()

selected_entries = {
    100:5,
    200:10,
    300:15,
    400:20
}

fn.pre_plot(1)

for i,n in enumerate(np.arange(0,20+pr.deltat,pr.deltat)):
    un =fn.ftcs(u)
    if i in selected_entries.keys():
        fn.plot([fn.x_val,un])
    u=un

fn.post_plot("x","u","FTCS Method","1_ftcs_out")
