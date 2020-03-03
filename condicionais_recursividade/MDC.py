def mdc(a, b):
    """Calcula o MDC de dois números recursivamente de acordo com o algorítmo de Euclides.
    :param a: valor inteiro
    :param b: valor inteiro
    :return: MDC de dois valores"""
    if b == 0:
        return  a
    else:
        return mdc(b, a%b)


def main():
    from random import randint

    a = randint(1, 1000)
    b = randint(1, 1000)
    print('A:', a)
    print('B:', b)
    result = mdc(a, b)
    print('MDC:', result)


if __name__ == '__main__':
    help(mdc)
    main()
