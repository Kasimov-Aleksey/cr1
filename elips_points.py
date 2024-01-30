def get_points(x, a, b):
    result = (x**3+a*x+b)%11
    result = 'y^2 = {}'.format(result)
    return result

for i in range(-6, 7):
    print('x= {}; '.format(i), get_points(x=i, a=6, b=3))