import math
import numpy as np

# Euclidean distance - get those that are <= the threshold and store them in
# a separate list. Then you can loop over and plot them.

def EuclideanDist(coordinates, threshold=5):
    qualified = []
    for i in range(0,len(coordinates)-1):
        try:
            coordinate = coordinates[i]
        except IndexError:
            break

        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]
        for i in range(i, len(coordinates)-1):
            try:
                comparison_coord = coordinates[i+1]
            except IndexError:
                break
            xComp = comparison_coord[0]
            yComp = comparison_coord[1]
            zComp = comparison_coord[2]

            xDistance = abs(x - xComp)
            yDistance = abs(y - yComp)
            zDistance = abs(z - zComp)

            distance = math.sqrt((xDistance**2 + yDistance**2 + zDistance**2))

            if distance <= threshold:
                tuple = (coordinate.tolist(), comparison_coord.tolist())
                qualified.append(tuple)
    
    return qualified

"""
The list does not need to go through every single combination;
only those that it has not previously seen.

So, loop through the list comparing the distance to all other items in the list then remove that item.

"""