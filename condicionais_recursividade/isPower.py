def is_power(a, b):
    """Verifica se a é potência de b recursivamente
    :param a: valor de um inteiro a
    :param b: valor de um inteiro b
    :return: booleano
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception('is_power() aceita apenas inteiros.')
    if a % b == 0:
        if a == b:
            return True
        else: 
            return is_power(a/b, b)
    return False


def main():
    try:
        a = 1.2
        b = 2
        power = is_power(a, b)
        print(power)
    except Exception as error:
        print('Exceção encontrada:', error)
        exit()


if __name__ == '__main__':
    main()
