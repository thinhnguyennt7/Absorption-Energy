from ase.spacegroup import crystal
from ase.build import surface
from ase.visualize import view

a=4.6
c=2.95
rutile=crystal(['Mo','O'],basis=[(0,0,0),(0.3,0.3,0.0)],
               spacegroup=136,cellpar=[a,a,c,90,90,90])

slab=surface(rutile,(1,1,0),2 #different layers by changing this value)
slab.center(vacuum=10,axis=2)

slab_repeat=slab.repeat((1,2,1))

view(slab)
view(slab_repeat)
