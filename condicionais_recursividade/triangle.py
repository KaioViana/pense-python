def is_triangle(a=1, b=1, c=1):
    if ((a - b) < c < (a + b)) and ((a - c) < b < (a + c)) and ((b - c) < a < (b +c)):
        return (True, vars())
    else: return (False, vars())


def classify_triangle(is_triangle):
    from math import degrees, acos


    if is_triangle[0]:
        triangle = is_triangle[1]
        a = triangle['a']
        b = triangle['b']
        c = triangle['c']

        ang_a = degrees(acos(((b**2 + c**2) - (a**2))/(2*b*c)))
        ang_b = degrees(acos(((b**2 + a**2) - (c**2))/(2*b*a)))
        ang_c = 180 - (ang_a + ang_b)
        print(f'{ang_a:.1f}')
        print(f'{ang_b:.1f}')
        print(f'{ang_c:.1f}')
    else: print('Impossível formar um triângulo')


def main():
    a = 90
    b = 128
    c = 130
    triangle = is_triangle(a, b, c)
    classify_triangle(triangle)


if __name__ == '__main__':
    main()
