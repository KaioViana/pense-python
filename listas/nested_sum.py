def nested_sum(l):
    """Faz a soma de valores de uma lista aninhada.
    :param l: lista aninhada
    :return: retorna a soma dos valores da lista aninhada
    """
    s = 0 # soma
    for values in l:
        s += sum(values)
    return s


def main():
    l = [[1,2,3], [4,5,6]]
    s = nested_sum(l)
    print(s)


if __name__ == '__main__':
    main()
