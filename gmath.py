import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

import math

def make_ccw(triangle):
    if not counter_clockwise(triangle[0], triangle[1], triangle[2]):
        triangle = [triangle[0], triangle[2], triangle[1]]
    return triangle

def counter_clockwise(p1, p2, p3):
    x_1, y_1 = p1[0], p1[1]
    x_2, y_2 = p2[0], p2[1]
    x_3, y_3 = p3[0], p3[1]
    val = (y_2 - y_1) * (x_3 - x_2) - (y_3 - y_2) * (x_2 - x_1)
    return val <= 0

def find_ear(pointlist):
  # This algorithm is based off the Two Ears Theorem.
  # Every simple polygon with 4 or more sides has at least two non-overlapping ears.
  i = 0
  while True:
    if convex(pointlist, i):
      if not concave(pointlist, i):
        break
    else:
      i += 1
  return i

def convex(pointlist, i):
    return find_angle(pointlist, i-1, i, (i+1) % len(pointlist)) < 180

def concave(pointlist, i):
    angle_1 = find_angle(pointlist, i-1, i, (i+1) % len(pointlist))
    angle_2 = find_angle(pointlist, i, (i+1) % len(pointlist), i-1)
    angle_3 = find_angle(pointlist, (i+1) % len(pointlist), i-1, i)
    return angle_1 >= 180 or angle_2 >= 180 or angle_3 >= 180

def find_angle(pointlist, a, b, c):
    a_0, a_1 = pointlist[a][0], pointlist[a][1]
    b_0, b_1 = pointlist[b][0], pointlist[b][1]
    c_0, c_1 = pointlist[c][0], pointlist[c][1]
    BA = (a_0-b_0, a_1-b_1)
    BC = (c_0-b_0, c_1-b_1)
    cosine_of_angle = (BA[0]*BC[0] + BA[1]*BC[1]) / (find_magnitude(BA) * find_magnitude(BC))
    angle = math.acos(cosine_of_angle)
    return math.degrees(angle)

def find_magnitude(vector):
  return math.sqrt(vector[0]**2 + vector[1]**2)

#lighting functions
def get_lighting(normal, view, ambient, light, symbols, reflect ):

    n = normal[:]
    normalize(n)
    normalize(light[LOCATION])
    normalize(view)
    r = symbols[reflect][1]

    a = calculate_ambient(ambient, r)
    d = calculate_diffuse(light, r, n)
    s = calculate_specular(light, r, view, n)

    i = [0, 0, 0]
    i[RED] = int(a[RED] + d[RED] + s[RED])
    i[GREEN] = int(a[GREEN] + d[GREEN] + s[GREEN])
    i[BLUE] = int(a[BLUE] + d[BLUE] + s[BLUE])
    limit_color(i)

    return i

def calculate_ambient(alight, reflect):
    a = [0, 0, 0]
    a[RED] = alight[RED] * reflect['red'][AMBIENT]
    a[GREEN] = alight[GREEN] * reflect['green'][AMBIENT]
    a[BLUE] = alight[BLUE] * reflect['blue'][AMBIENT]
    return a

def calculate_diffuse(light, reflect, normal):
    d = [0, 0, 0]

    dot = dot_product( light[LOCATION], normal)

    dot = dot if dot > 0 else 0
    d[RED] = light[COLOR][RED] * reflect['red'][DIFFUSE] * dot
    d[GREEN] = light[COLOR][GREEN] * reflect['green'][DIFFUSE] * dot
    d[BLUE] = light[COLOR][BLUE] * reflect['blue'][DIFFUSE] * dot
    return d

def calculate_specular(light, reflect, view, normal):
    s = [0, 0, 0]
    n = [0, 0, 0]

    result = 2 * dot_product(light[LOCATION], normal)
    n[0] = (normal[0] * result) - light[LOCATION][0]
    n[1] = (normal[1] * result) - light[LOCATION][1]
    n[2] = (normal[2] * result) - light[LOCATION][2]

    result = dot_product(n, view)
    result = result if result > 0 else 0
    result = pow( result, SPECULAR_EXP )

    s[RED] = light[COLOR][RED] * reflect['red'][SPECULAR] * result
    s[GREEN] = light[COLOR][GREEN] * reflect['green'][SPECULAR] * result
    s[BLUE] = light[COLOR][BLUE] * reflect['blue'][SPECULAR] * result
    return s

def limit_color(color):
    color[RED] = 255 if color[RED] > 255 else color[RED]
    color[GREEN] = 255 if color[GREEN] > 255 else color[GREEN]
    color[BLUE] = 255 if color[BLUE] > 255 else color[BLUE]

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
