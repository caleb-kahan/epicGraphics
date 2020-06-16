# EpicGraphics

Names: Caleb Kahan (PD 4), Eric Shau (PD 5)

## MDL Commands

- shape
- extrusion
- revolution

## shape

```
shape [name] [plane] [pointlist]
```

The program stores the shape with that name as described by the plane (xy, xz, or yz) and the pointlist (a list of 2d points on that plane).

**Example**:
```
shape caleb xy [(-50,0),(50,0),(50,100),(-50,100)]
```

## extrusion

```
extrusion [shape_name] [constants] [length]
```

The program creates an extrusion of the shape stored previously that has the color described by the constants and extending [length] units in the positive direction.

**NOTE**: The extrusion command only works with **CONVEX** shapes.

**Example**:
```
extrusion caleb shiny_purple 60
```

## revolution

```
revolution [shape_name] [constants] [axis] [axis number]
```

The program creates a revolution of the shape stored previously that has the color described by the constants and revolving 360 degrees around the [axis] = [axis number]. [axis] can be x, y, or z, and [axis number] can be any number.

**Example**:
```
revolution caleb shiny_purple y 0
```
