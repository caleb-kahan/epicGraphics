# EpicGraphics

Names: Caleb Kahan (PD 4), Eric Shau (PD 5)

## MDL Commands

- shape
- extrusion
- revolution
- print

## print

```
print [text]
```

This was created specfically for the readibility of the testing by you. With no argument, "print" prints a new line helpful for seperating text, and with an argument prints the text, given there are no spaces (No regex manipulation on our part for this). 


## shape

```
shape [name] [plane] [pointlist]
```

The program stores the shape with that name as described by the plane (xy, xz, or yz) and the pointlist (a list of 2d points on that plane). Using some regex manipulation in the mdl code, we were able to extract an indefinite amount of points and then used the python "eval" function to convert the string to an python object.

**Example**:
```
shape caleb xy [(-50,0),(50,0),(50,100),(-50,100)]
```

## extrusion

```
extrusion [shape_name] [constants] [length]
```

The program creates an extrusion of the shape stored previously that has the color described by the constants and extending [length] units in the positive direction. We devised our own algirithm for the body of the 3-d solid, and used an ear-clipping algirthm to fill in the polygon faces on "top" and "bottom"

**NOTE**: The extrusion command works best with convex shapes.

**Example**:
```
extrusion caleb shiny_purple 60
```

## revolution

```
revolution [shape_name] [constants] [axis] [axis number]
```

The program creates a revolution of the shape stored previously that has the color described by the constants and revolving 360 degrees around the [axis] = [axis number]. [axis] can be x, y, or z, and [axis number] can be any number. The bigger the axis number, the farther away the object will be from the axis of rotation, and the bigger the radius the revolution will be. This can help create holes in the 3d object.

**Example**:
```
revolution caleb shiny_purple y 0
```

## How to Run
```
You can test the two submission files to the gallery by either entering "make gallery1" or "make gallery2"
```
```
You can also a test a long submission file testing print, Revolution, Extrusion, and shape, which displays several objects one a time by just entering "make"
```
