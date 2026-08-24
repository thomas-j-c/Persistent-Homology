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
    coordinates.append(atom.get_coord().tolist())
    


#Vietoris-Rips filtration
filtration = gd.RipsComplex(points=coordinates, max_edge_length=3)
tree = filtration.create_simplex_tree()
tree.compute_persistence()
pairs = tree.persistence_pairs()

#intervals = tree.persistence_intervals_in_dimension(3)
#print(intervals)


fig = plt.figure()
ax = fig.add_subplot()

births = []
deaths = []

for pair in pairs:
    try:
        births.append(pair[1][0])
        deaths.append(pair[1][1])
    except IndexError:
        continue

ax.scatter(births, deaths, s=1)

plt.show()

