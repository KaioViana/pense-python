def middle(t):
    """Recebe uma lista e retorna uma cópia dela contendo apenas os valores do meio
    
    :param t: lista de valores numéricos
    :return: cópia da lista t apenas com os valores do meio
    """
    return t[1:-1]


def main():
    t = [1,2,3,4]
    t2 = middle(t)
    print(t2)


if __name__ == '__main__':
    main()
