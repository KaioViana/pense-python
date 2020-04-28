def cumsum(t):
    """Recebe uma lista de valores numéricos e retorna uma nova lista
    com a soma cumulativa da primeira.
    
    :param t: lista contendo valores numéricos
    :return: lista t2 com a soma cumulativa
    """
    t2 = []
    for num in t:
        if t2:
            t2.append(num + t2[-1])
        else:
            t2.append(num)
    return t2


def main():
    t = [1,1,1]
    t2 = cumsum(t)
    print(t2)


if __name__ == '__main__':
    main()
