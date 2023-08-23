points = [[-1,2],[-2,3],[-2,1],[-1,3],[-1,4],[-1,5]]

def new_points (x): # превращение точки А в началоо оординат, и проецирвание остальных точек массива относительно изменений в координатах А
    _x0 = x[0][0]
    _y0 = x[0][1]
    i = 0
    for el in x:
        if el[0] >= 0:
            el[0] = el[0] - _x0
            if el[1] > 0:
                el[1] = el[1] - _y0
            else:
                el[1] = el[1] + (_y0)*(-1)
        else:
            el[0] = el[0] + (_x0)*(-1)
            if el[1] > 0:
                el[1] = el[1] - _y0
            else:
                el[1] = el[1] + (_y0)*(-1)
        i += 1
    return x

print(new_points(points))
_points = sorted(new_points(points))

def needed_points(p): # фунция для обнаружения ближайших точек вокруг А
    r = 3 #радиус точек вокруг А
    a_round_points = []
    for el in p:
        if (el[0] <= 0 and el[0] >= -r) and (el[1] <= r and el[1] >= -r):
            a_round_points.append(el)
    return a_round_points

A_points = sorted(needed_points(_points))
print(A_points)