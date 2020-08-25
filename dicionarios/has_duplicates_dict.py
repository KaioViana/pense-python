def has_duplicates(t):
    """Recebe uma lista e verifica se nela há valores duplicados.
        :param t: lista a ser analizada.
        :var d: dicionário para armazenamento de valores.
        :return: boolean.
    """
    d = dict()

    for value in t:
        if value in d:
            return True
        d[value] = True
    return False


def main():
    t = [1,2,3,4]
    t1 = [1,2,3,2]
    t2 = [1,2,2,3]

    print(has_duplicates(t))
    print(has_duplicates(t1))
    print(has_duplicates(t2))


if __name__ == '__main__':
    main()
