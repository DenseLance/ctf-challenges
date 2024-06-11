# forensics/sheep

<p align = "center"><img src="challenge.JPG" alt="alt text" width="75%" height="75%" /></p>

<details> 
  <summary><b>Hint 1</b></summary>
   Figure out what type of file it is and see if there are tools you can use or modify.
</details>

They really just said "baa", refused to elaborate, and left. The file provided was a `.shp` file, which points us to the ESRI shapefile format. Searching the first 4 bytes of the file `00 00 27 0A` confirmed that guess. So, it wasn't a sheep after all!

We used the `pyshp` module to read the image. As plot points were provided for each geometric shape in the file, we simply plot them using `matplotlib`.

```python
import shapefile
import matplotlib.pyplot as plt

with shapefile.Reader("sheep.shp") as shape:
    shapes = shape.shapes()
    points = [shapes[i].points for i in range(len(shapes))]

for point in points:
    x, y = zip(*point)
    plt.scatter(x, y)

plt.show()
```

We managed to get the flag! 

<p align = "center"><img src="sheep.PNG" alt="alt text" width="75%" height="75%" /></p>

```
bcactf{SHaPE_f1lEd_b54a11ac9c87c8}
```