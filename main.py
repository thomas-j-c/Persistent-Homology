print("Hello World!")

import gudhi as gd
from Bio.PDB import *
import matplotlib.pyplot as plt
from distance import EuclideanDist

parser = MMCIFParser()
structure = parser.get_structure("MyFirstStructure", "data/364D.cif")
atoms = structure.get_atoms()
coordinates = []
for atom in atoms:
    coordinates.append(atom.get_coord())

qualified = EuclideanDist(coordinates, 5)
print(qualified)

"""
filtration = gd.RipsComplex(points=coordinates, max_edge_length=3)
tree = filtration.create_simplex_tree()
tree.collapse_edges()
pairs = tree.persistence_pairs()

print(pairs[1])

atoms = structure.get_atoms()
xCoords = []
yCoords = []
zCoords = []

fig = plt.figure()
ax = fig.add_subplot(projection="3d")


for atom in atoms:
    coordinates = atom.get_coord().tolist()
    xCoords.append(coordinates[0])
    yCoords.append(coordinates[1])
    zCoords.append(coordinates[2])
    #coordinates.append(atom.get_coord().tolist())
    

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(xCoords, yCoords, zCoords, s=1)
plt.show()


#Vietoris-Rips filtration
filtration = gd.RipsComplex(points=coordinates, max_edge_length=3)
tree = filtration.create_simplex_tree()
tree.compute_persistence()
pairs = tree.persistence_pairs()

#intervals = tree.persistence_intervals_in_dimension(3)
#print(intervals)


Try a simpler structure like the one in the arXiv paper, 
try visualising that too with the links between the points.


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
"""
