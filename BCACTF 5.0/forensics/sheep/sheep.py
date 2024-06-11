import shapefile
import matplotlib.pyplot as plt

with shapefile.Reader("sheep.shp") as shape:
    shapes = shape.shapes()
    points = [shapes[i].points for i in range(len(shapes))]

for point in points:
    x, y = zip(*point)
    plt.scatter(x, y)

plt.show()
