def mysqrt(n):
    """Cálcula a raiz quadrada de um número utilizando o método de Newton
    :param n: número a ser calculado
    :param x: estimativa da raiz
    :return: valor da raiz quadrada de n"""
    x = 1
    while True:
        y = (x + n/x) / 2
        if y == x:
            return y
        x = y


def test_square_root():
    """Compara mysqrt com math.sqrt()"""
    from math import sqrt


    n = 1

    print(f'{"a":<20} {"mysqrt(a)":<20} {"math.sqrt(a)":<20} {"diff":<20}')
    print(f'{"=":=<20}{"=":=<20}{"=":=<20}{"=":=<20}')
    while n <= 9:
        x = mysqrt(n)
        y = sqrt(n)
        print(f'{n:<20} {x:<20} {y:<20} {abs(x-y):<20}')
        n += 1


def main():
    test_square_root()

if __name__ == '__main__':
    main()
