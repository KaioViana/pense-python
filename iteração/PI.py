def factorial(n):
    """Calcula a fotorial recursivamente
    :param n: fatorial a ser calculada
    :return: fatorial de n"""
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def PI_estimate():
    """Faz uma estimativa do pi usando o cálculo de séries infinitas do Ramanujan
    :return: estimativa de pi"""
    from math import sqrt


    k = 0
    total = 0
    factor = 2*sqrt(2)/9801
    while True:
        num = factorial(4*k)*(1103 + 26390*k)
        den = factorial(k)**4*396**(4*k)
        term = factor * num/den
        total += term
        
        if abs(term) < 1e-15:
            break
        k += 1
    return 1/total


def main():
    from math import pi
    print('Série infinita de Ramanujan',PI_estimate())
    print('math.pi', pi)


if __name__ == '__main__':
    main()
