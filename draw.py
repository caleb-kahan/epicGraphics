from display import *
from matrix import *
from gmath import *

def add_extrusion(polygons, name, length, symbols):
    # Shapes/lids
    break_shape(name, symbols, polygons, 0)
    break_shape(name, symbols, polygons, length)
    # Actual extrusion
    shape = symbols[name]
    points = shape[1]['points']
    generator = generate_extrusion(name, length, symbols)

    mainTriangle = [points[0],points[1],points[2]]
    flip = False
    if counter_clockwise(mainTriangle[0],mainTriangle[1],mainTriangle[2]):
        flip = True

    for start in range(len(points)):
        if start == len(points) - 1:
            triangle1 = [generator[start],
                         generator[start+len(points)],
                         generator[start+1]
                        ]
            triangle2 = [generator[start],
                         generator[start+1],
                         generator[0]
                        ]

            if flip:
                tmp = triangle1[1][:]
                triangle1[1] = triangle1[2][:]
                triangle1[2] = tmp

            if flip:
                tmp = triangle2[1][:]
                triangle2[1] = triangle2[2][:]
                triangle2[2] = tmp

            add_polygon( polygons,
                         triangle1[0][0],
                         triangle1[0][1],
                         triangle1[0][2],
                         triangle1[1][0],
                         triangle1[1][1],
                         triangle1[1][2],
                         triangle1[2][0],
                         triangle1[2][1],
                         triangle1[2][2])
            add_polygon( polygons,
                         triangle2[0][0],
                         triangle2[0][1],
                         triangle2[0][2],
                         triangle2[1][0],
                         triangle2[1][1],
                         triangle2[1][2],
                         triangle2[2][0],
                         triangle2[2][1],
                         triangle2[2][2])
        else:
            triangle1 = [generator[start],
                         generator[start+len(points)],
                         generator[start+len(points)+1]
                        ]
            triangle2 = [generator[start],
                         generator[start+1+len(points)],
                         generator[start+1]
                        ]

            if flip:
                tmp = triangle1[1][:]
                triangle1[1] = triangle1[2][:]
                triangle1[2] = tmp

            if flip:
                tmp = triangle2[1][:]
                triangle2[1] = triangle2[2][:]
                triangle2[2] = tmp

            add_polygon( polygons,
                             triangle1[0][0],
                             triangle1[0][1],
                             triangle1[0][2],
                             triangle1[1][0],
                             triangle1[1][1],
                             triangle1[1][2],
                             triangle1[2][0],
                             triangle1[2][1],
                             triangle1[2][2])
            add_polygon( polygons,
                         triangle2[0][0],
                         triangle2[0][1],
                         triangle2[0][2],
                         triangle2[1][0],
                         triangle2[1][1],
                         triangle2[1][2],
                         triangle2[2][0],
                         triangle2[2][1],
                         triangle2[2][2])


def generate_extrusion(name, length, symbols):
    shape = symbols[name]
    generator = []
    plane = shape[1]['plane']
    points = shape[1]['points']
    if length == 0:
        print('Need at least one thickness to proceed')
        return
    for i in [0, abs(length)-1]:
        for j in range(len(points)):
            if plane == 'xy':
                x = points[j][0]
                y = points[j][1]
                z = i
            elif plane == 'xz':
                x = points[j][0]
                y = i
                z = points[j][1]
            elif plane == 'yz':
                x = i
                y = points[j][0]
                z = points[j][1]
            generator.append( [x, y, z] )
    return generator

def break_shape(name, symbols, polygons, other_coordinate):
    shape = symbols[name]
    plane = shape[1]['plane']
    points = shape[1]['points']
    copy_points = [point[:] for point in points]
    while len(copy_points) > 2:
        i = find_ear(copy_points)
        p1 = copy_points[i-1]
        p2 = copy_points[i]
        p3 = copy_points[(i+1) % len(copy_points)]
        triangle = [p1, p2, p3]
        triangle = make_ccw(triangle)
        if plane == 'xy':
            add_polygon(polygons,
                        triangle[0][0],
                        triangle[0][1],
                        other_coordinate,
                        triangle[1][0],
                        triangle[1][1],
                        other_coordinate,
                        triangle[2][0],
                        triangle[2][1],
                        other_coordinate)
        elif plane == 'xz':
            add_polygon(polygons,
                        triangle[0][0],
                        other_coordinate,
                        triangle[0][1],
                        triangle[1][0],
                        other_coordinate,
                        triangle[1][1],
                        triangle[2][0],
                        other_coordinate,
                        triangle[2][1])
        elif plane == 'yz':
            add_polygon(polygons,
                        other_coordinate,
                        triangle[0][0],
                        triangle[0][1],
                        other_coordinate,
                        triangle[0][0],
                        triangle[0][1],
                        other_coordinate,
                        triangle[0][0],
                        triangle[0][1])
        else:
            print("Error: Invalid plane.")
            break
        copy_points.pop(i)


def add_rotation(border1,border2,polygons):
    length = len(border1)
    for i in range(length):
        if border1[(i+1)%length] != border2[(i+1)%length]:
            add_polygon(polygons,
                    border2[(i+1)%length][0],
                    border2[(i+1)%length][1],
                    border2[(i+1)%length][2],
                    border1[(i+1)%length][0],
                    border1[(i+1)%length][1],
                    border1[(i+1)%length][2],
                    border1[i][0],
                    border1[i][1],
                    border1[i][2]

                    )

        if border1[i] != border2[i]:
            add_polygon(polygons,
                    border2[i][0],
                    border2[i][1],
                    border2[i][2],
                    border2[(i+1)%length][0],
                    border2[(i+1)%length][1],
                    border2[(i+1)%length][2],
                    border1[i][0],
                    border1[i][1],
                    border1[i][2])

def findTranslationArguments(name,symbols,length):
    shape = symbols[name]
    plane = shape[1]['plane']
    if plane == "xy":
        return (0,0,length)
    if plane == "yz":
        return (length,0,0)
    if plane == "xz":
        return (0,length,0)

def modifyBorder(border,plane):
    newBorder = []
    for i in range(len(border)):
        if plane == 'xy':
            x = border[i][0]
            y = border[i][1]
            z = 0
        elif plane == 'xz':
            x = border[i][0]
            y = 0
            z = border[i][1]
        elif plane == 'yz':
            x = 0
            y = border[i][0]
            z = border[i][1]
        newBorder.append([x,y,z,1])
    return newBorder

def draw_scanline(x0, z0, x1, z1, y, screen, zbuffer, color):
    if x0 > x1:
        tx = x0
        tz = z0
        x0 = x1
        z0 = z1
        x1 = tx
        z1 = tz

    x = x0
    z = z0
    delta_z = (z1 - z0) / (x1 - x0 + 1) if (x1 - x0 + 1) != 0 else 0

    while x <= x1:
        plot(screen, zbuffer, color, x, y, z)
        x+= 1
        z+= delta_z

def scanline_convert(polygons, i, screen, zbuffer, color):
    flip = False
    BOT = 0
    TOP = 2
    MID = 1

    points = [ (polygons[i][0], polygons[i][1], polygons[i][2]),
               (polygons[i+1][0], polygons[i+1][1], polygons[i+1][2]),
               (polygons[i+2][0], polygons[i+2][1], polygons[i+2][2]) ]

    # alas random color, we hardly knew ye
    #color = [0,0,0]
    #color[RED] = (23*(i/3)) %256
    #color[GREEN] = (109*(i/3)) %256
    #color[BLUE] = (227*(i/3)) %256

    points.sort(key = lambda x: x[1])
    x0 = points[BOT][0]
    z0 = points[BOT][2]
    x1 = points[BOT][0]
    z1 = points[BOT][2]
    y = int(points[BOT][1])

    distance0 = int(points[TOP][1]) - y * 1.0 + 1
    distance1 = int(points[MID][1]) - y * 1.0 + 1
    distance2 = int(points[TOP][1]) - int(points[MID][1]) * 1.0 + 1

    dx0 = (points[TOP][0] - points[BOT][0]) / distance0 if distance0 != 0 else 0
    dz0 = (points[TOP][2] - points[BOT][2]) / distance0 if distance0 != 0 else 0
    dx1 = (points[MID][0] - points[BOT][0]) / distance1 if distance1 != 0 else 0
    dz1 = (points[MID][2] - points[BOT][2]) / distance1 if distance1 != 0 else 0

    while y <= int(points[TOP][1]):
        if ( not flip and y >= int(points[MID][1])):
            flip = True

            dx1 = (points[TOP][0] - points[MID][0]) / distance2 if distance2 != 0 else 0
            dz1 = (points[TOP][2] - points[MID][2]) / distance2 if distance2 != 0 else 0
            x1 = points[MID][0]
            z1 = points[MID][2]

        #draw_line(int(x0), y, z0, int(x1), y, z1, screen, zbuffer, color)
        draw_scanline(int(x0), z0, int(x1), z1, y, screen, zbuffer, color)
        x0+= dx0
        z0+= dz0
        x1+= dx1
        z1+= dz1
        y+= 1


# def find_polygon(polygons,x0,y0,z0,x1,y1,z1,x2,y2,z2):
#     for i in range(0,len(polygons),3):
#         triangle = polygons[i:i+3]
#         if [x0,y0,z0,1] in triangle and [x1,y1,z1,1] in triangle and [x2,y2,z2,1] in triangle:
#             return False
#     return True

def add_polygon( polygons, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    # if find_polygon(polygons,x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
        # add_point(polygons, x0, y0, z0)
        # add_point(polygons, x1, y1, z1)
        # add_point(polygons, x2, y2, z2)
    add_point(polygons, x0, y0, z0)
    add_point(polygons, x1, y1, z1)
    add_point(polygons, x2, y2, z2)

def draw_polygons( polygons, screen, zbuffer, view, ambient, light, symbols, reflect):
    if len(polygons) < 2:
        print('Need at least 3 points to draw')
        return

    point = 0
    while point < len(polygons) - 2:

        normal = calculate_normal(polygons, point)[:]
        #print normal
        if normal[2] > 0:
            color = get_lighting(normal, view, ambient, light, symbols, reflect )
            scanline_convert(polygons, point, screen, zbuffer, color)
        point+= 3

def draw_surface(surface, screen, zbuffer, view, ambient, light, symbols, reflect, border):
    #Any combination of points works
    p1 = [border[2][0],border[2][1],border[2][2]]
    p2 = [border[3][0],border[3][1],border[3][2]]
    p3 = [border[4][0],border[4][1],border[4][2]]

    polygons = [p1,p2,p3]

    if calculate_normal(polygons,0)[:][2] > 0:
        polygons = [p1,p2,p3]
    elif calculate_normal(polygons,0)[:][2] < 0:
        polygons = [p1,p3,p2]
    elif calculate_normal(polygons,0)[:][2] < 0:
        polygons = [p2,p1,p3]
    elif calculate_normal(polygons,0)[:][2] < 0:
        polygons = [p2,p3,p1]
    elif calculate_normal(polygons,0)[:][2] < 0:
        polygons = [p3,p1,p2]
    elif calculate_normal(polygons,0)[:][2] < 0:
        polygons = [p3,p2,p1]

    normal = calculate_normal(polygons, 0)[:]

        #color = get_lighting(normal, view, ambient, light, symbols, reflect )
    color = get_lighting(normal, view, ambient, light, symbols, reflect )
    for i in range(len(surface)):
        #print(surface[i])
        plot(screen,zbuffer,color,int(surface[i][0]),int(surface[i][1]),int(surface[i][2]))


def add_box( polygons, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    #front
    add_polygon(polygons, x, y, z, x1, y1, z, x1, y, z)
    add_polygon(polygons, x, y, z, x, y1, z, x1, y1, z)

    #back
    add_polygon(polygons, x1, y, z1, x, y1, z1, x, y, z1)
    add_polygon(polygons, x1, y, z1, x1, y1, z1, x, y1, z1)

    #right side
    add_polygon(polygons, x1, y, z, x1, y1, z1, x1, y, z1)
    add_polygon(polygons, x1, y, z, x1, y1, z, x1, y1, z1)
    #left side
    add_polygon(polygons, x, y, z1, x, y1, z, x, y, z)
    add_polygon(polygons, x, y, z1, x, y1, z1, x, y1, z)

    #top
    add_polygon(polygons, x, y, z1, x1, y, z, x1, y, z1)
    add_polygon(polygons, x, y, z1, x, y, z, x1, y, z)
    #bottom
    add_polygon(polygons, x, y1, z, x1, y1, z1, x1, y1, z)
    add_polygon(polygons, x, y1, z, x, y1, z1, x1, y1, z1)

def add_sphere(polygons, cx, cy, cz, r, step ):
    points = generate_sphere(cx, cy, cz, r, step)

    lat_start = 0
    lat_stop = step
    longt_start = 0
    longt_stop = step

    step+= 1
    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):

            p0 = lat * step + longt
            p1 = p0+1
            p2 = (p1+step) % (step * (step-1))
            p3 = (p0+step) % (step * (step-1))

            if longt != step - 2:
                add_polygon( polygons, points[p0][0],
                             points[p0][1],
                             points[p0][2],
                             points[p1][0],
                             points[p1][1],
                             points[p1][2],
                             points[p2][0],
                             points[p2][1],
                             points[p2][2])
            if longt != 0:
                add_polygon( polygons, points[p0][0],
                             points[p0][1],
                             points[p0][2],
                             points[p2][0],
                             points[p2][1],
                             points[p2][2],
                             points[p3][0],
                             points[p3][1],
                             points[p3][2])


def generate_sphere( cx, cy, cz, r, step ):
    points = []

    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        for circle in range(circ_start, circ_stop+1):
            circ = circle/float(step)

            x = r * math.cos(math.pi * circ) + cx
            y = r * math.sin(math.pi * circ) * math.cos(2*math.pi * rot) + cy
            z = r * math.sin(math.pi * circ) * math.sin(2*math.pi * rot) + cz

            points.append([x, y, z])
            #print 'rotation: %d\tcircle%d'%(rotation, circle)
    return points

def add_torus(polygons, cx, cy, cz, r0, r1, step ):
    points = generate_torus(cx, cy, cz, r0, r1, step)

    lat_start = 0
    lat_stop = step
    longt_start = 0
    longt_stop = step

    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):

            p0 = lat * step + longt;
            if (longt == (step - 1)):
                p1 = p0 - longt;
            else:
                p1 = p0 + 1;
            p2 = (p1 + step) % (step * step);
            p3 = (p0 + step) % (step * step);

            add_polygon(polygons,
                        points[p0][0],
                        points[p0][1],
                        points[p0][2],
                        points[p3][0],
                        points[p3][1],
                        points[p3][2],
                        points[p2][0],
                        points[p2][1],
                        points[p2][2] )
            add_polygon(polygons,
                        points[p0][0],
                        points[p0][1],
                        points[p0][2],
                        points[p2][0],
                        points[p2][1],
                        points[p2][2],
                        points[p1][0],
                        points[p1][1],
                        points[p1][2] )


def generate_torus( cx, cy, cz, r0, r1, step ):
    points = []
    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        for circle in range(circ_start, circ_stop):
            circ = circle/float(step)

            x = math.cos(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cx;
            y = r0 * math.sin(2*math.pi * circ) + cy;
            z = -1*math.sin(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cz;

            points.append([x, y, z])
    return points


def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    i = 1

    while i <= step:
        t = float(i)/step
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        i+= 1

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = t * (t * (xcoefs[0] * t + xcoefs[1]) + xcoefs[2]) + xcoefs[3]
        y = t * (t * (ycoefs[0] * t + ycoefs[1]) + ycoefs[2]) + ycoefs[3]
        #x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        #y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        i+= 1


def draw_lines( matrix, screen, zbuffer, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   matrix[point][2],
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   matrix[point+1][2],
                   screen, zbuffer, color, False, None)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( x0, y0, z0, x1, y1, z1, screen, zbuffer, color, addition, tmp):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        zt = z0
        x0 = x1
        y0 = y1
        z0 = z1
        x1 = xt
        y1 = yt
        z1 = zt

    x = x0
    y = y0
    z = z0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    wide = False
    tall = False

    if ( abs(x1-x0) >= abs(y1 - y0) ): #octants 1/8
        wide = True
        loop_start = x
        loop_end = x1
        dx_east = dx_northeast = 1
        dy_east = 0
        d_east = A
        distance = x1 - x + 1
        if ( A > 0 ): #octant 1
            d = A + B/2
            dy_northeast = 1
            d_northeast = A + B
        else: #octant 8
            d = A - B/2
            dy_northeast = -1
            d_northeast = A - B

    else: #octants 2/7
        tall = True
        dx_east = 0
        dx_northeast = 1
        distance = abs(y1 - y) + 1
        if ( A > 0 ): #octant 2
            d = A/2 + B
            dy_east = dy_northeast = 1
            d_northeast = A + B
            d_east = B
            loop_start = y
            loop_end = y1
        else: #octant 7
            d = A/2 - B
            dy_east = dy_northeast = -1
            d_northeast = A - B
            d_east = -1 * B
            loop_start = y1
            loop_end = y

    dz = (z1 - z0) / distance if distance != 0 else 0

    while ( loop_start < loop_end ):
        if addition:
            tmp.append([x,y,z,1])
        else:
            plot( screen, zbuffer, color, x, y, z )
        if ( (wide and ((A > 0 and d > 0) or (A < 0 and d < 0))) or
             (tall and ((A > 0 and d < 0) or (A < 0 and d > 0 )))):

            x+= dx_northeast
            y+= dy_northeast
            d+= d_northeast
        else:
            x+= dx_east
            y+= dy_east
            d+= d_east
        z+= dz
        loop_start+= 1
    if addition:
        tmp.append([x,y,z,1])
    else:
        plot( screen, zbuffer, color, x, y, z )
