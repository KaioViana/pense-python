def is_triangle(a=1, b=1, c=1):
    """Verifica a condição de existência de um triângulo.
    :param a: medida do lado a
    :param b: medida do lado b
    :param c: medida do lado c
    :return: boolean, valores dos argumentos passados
    """
    if ((a - b) < c < (a + b)) and ((a - c) < b < (a + c)) and ((b - c) < a < (b +c)):
        return (True, vars())
    else: return (False, vars())


def classify_triangle(is_triangle):
    """Classifica um triângulo quanto à suas medidas e ângulos
    :param is_triangle: função de verificação de existência do triângulo
    :return: None
    """
    from math import degrees, acos


    classify = ''

    if is_triangle[0]:
        # fazendo atribuições das medidas
        triangle = is_triangle[1]
        a = triangle['a']
        b = triangle['b']
        c = triangle['c']

        # calculando os ângulos
        ang_a = degrees(acos(((b**2 + c**2) - (a**2))/(2*b*c)))
        ang_b = degrees(acos(((b**2 + a**2) - (c**2))/(2*b*a)))
        ang_c = 180 - (ang_a + ang_b)

        # classificando o triângulo quanto à medida de seus lados
        if a == b == c:
            classify = 'Triângulo equilátero '
        elif a == b or a == c or b == c:
            classify = 'Triângulo isósceles '
        else:
            classify = 'Triângulo escaleno '

        # classificando o triângulo quanto à medida dos seus ângulos
        if  ang_a < 90 and ang_b < 90 and ang_c < 90:
            classify += 'acutângulo.'
        elif ang_a > 90 or ang_b > 90 or ang_c > 90:
            classify += 'obtusângulo.'
        elif (ang_a == 90 and ang_b != 90 != ang_c) or (ang_b == 90 and ang_a != 90 != ang_c) or (ang_c == 90 and ang_b != 90 != ang_a):
            classify += 'retângulo.'

        # mostrando os lados
        print('VALORES DAS MEDIDAS DOS LADOS:')
        print(f'A: {a}')
        print(f'B: {b}')
        print(f'C: {c}\n')

        # mostrando ângulos
        print('VALORES DOS ÂNGULOS:')
        print(f'ang_a: {ang_a:.1f}°')
        print(f'ang_b: {ang_b:.1f}°')
        print(f'ang_c: {ang_c:.1f}°')
        print('soma:', str(ang_a + ang_b + ang_c) + '°\n')

        # mostrando a classificação do triângulo
        print('CLASSIFICAÇÃO DO TRIÂNGULO:')
        print(classify)
    else: print('Impossível formar um triângulo')


def main():
    from random import randint
    a = randint(3, 9)
    b = randint(3, 12)
    c = randint(3, 15)
    triangle = is_triangle(a, b, c)
    classify_triangle(triangle)


if __name__ == '__main__':
    main()
