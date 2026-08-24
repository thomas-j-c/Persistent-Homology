print("Hello World!")

import gudhi as gd
from Bio.PDB import *
import matplotlib.pyplot as plt

parser = MMCIFParser()
structure = parser.get_structure("MyFirstStructure", "data/9ZBV.cif")

# print(structure.center_of_mass())

atoms = structure.get_atoms()

coordinates = []

for atom in atoms:
    print(atom.coord)
#split coordinates into x,y, z lists then you can use them in matplotlib.
# add the project to git

plt.scatter()

