from ase import io
from ase.constraints import FixAtoms, FixBondLength
from espresso import espresso
from ase.optimize.minimahopping import MinimaHopping

atoms=io.read('converged.traj')

constraints=[FixAtoms(indices=[atom.index for atom in atoms if atom.index < 8]),
             FixBondLength(10,11),
             FixBondLength(9,10),
             FixBondLength(9,12),
             FixBondLength(9,13),
             FixBondLength(8,9),
             FixBondLength(8,14),
             FixBondLength(8,15),
             FixBondLength(8,16)]

atoms.set_constraint(constraints)

calcargs = dict(xc='BEEF-vdW',
        kpts=(3,3,1), #only need 1 kpt in z-direction
        pw=300.,
        dw=3000.,
        spinpol=True,
        convergence={'energy':1e-6,
                    'mixing':0.05,
                    'maxsteps':1000,
                    'diag':'david'},
        dipole={'status':True}, #dipole corrections True turns them on
        outdir ='esp.log')

calc= espresso(**calcargs)
atoms.set_calculator(calc)


hop = MinimaHopping(atoms=atoms)
hop()
