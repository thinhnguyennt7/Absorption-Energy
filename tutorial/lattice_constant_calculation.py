from ase.io import *
from espresso import espresso
from scipy.optimize import fmin
from copy import deepcopy as copy

calcargs = dict(xc='PBE',
        kpts=(5,7,1), #only need 1 kpt in z-direction
        pw=450,
        dw=4500,
        spinpol=True,
        convergence={'energy':1e-6,
                    'mixing':0.05,
                    'maxsteps':1000,
                    'diag':'david'},
        dipole={'status':True}, #dipole corrections True turns them on
        outdir ='esp.log',#save the espresso output at esp.log
                        )

def E_MoO2(abc, calcargs):
    a,b,c = abc
    orig = read('MoO2_110.traj')
    MoO2 = copy(orig)
    MoO2.set_cell([a,b,c],scale_atoms=True)
    calc = espresso(**calcargs)
    MoO2.set_calculator(calc)
    E = MoO2.get_potential_energy()
    MoO2.write('MoO2-'+str(round(a,2))+'-'+str(round(b,2))+'-'+str(round(c,2))+'.traj')
    return E

x0 = [3.755,3.921,15.497] #the initial value can be the experimental results from springer materials
xopt = fmin(E_MoO2,x0,args=(calcargs,))#optimize the lattice constant
f = open('latconst.txt','w')
f.write(xopt)
f.close()
