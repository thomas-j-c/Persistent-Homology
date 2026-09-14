import gudhi as gd
from Bio.PDB import *
import matplotlib.pyplot as plt
from distance import EuclideanDist

parser = MMCIFParser()
structure = parser.get_structure("MyFirstStructure", "data/9ZBV.cif")
atoms = structure.get_atoms()

xs = []
ys = []
zs = []

atomsList = [x.get_coord() for x in atoms]

filtration = gd.RipsComplex(points=atomsList, max_edge_length=0.5)
tree = filtration.create_simplex_tree(max_dimension=3)

rips = tree.get_filtration()

for splx in list(rips):
    minimum = 30
    if len(splx[0]) == 2:
        if splx[1] < minimum:
            minimum = splx[1]

        vertices = splx[0] ## List of 3 vertices

        for vertex in vertices:
            atomCoords = atomsList[vertex-1].tolist()
            xs.append(atomCoords[0])
            ys.append(atomCoords[1])
            zs.append(atomCoords[2])
                

print(minimum)
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot(xs, ys)
plt.show()

## Use the github thing on firefox
"""
points = np.array([filtration.get_point(i) for i in range(tree.num_vertices())])

triangles = np.array([s[0] for s in tree.get_skeleton(2) if len(s[0]) <= 2 and s[1] <= 0.005])

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=triangles)
plt.show()


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

for pair in qualified:
    xs = [pair[0][0], pair[1][0]]
    ys = [pair[0][1], pair[1][1]]
    zs = [pair[0][2], pair[1][2]]
    ax.plot(xs, ys, zs)

plt.show()



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
"""
