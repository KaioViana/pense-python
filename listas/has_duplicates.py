def has_duplicates(t):
    """Recebe uma lista e verifica se há elementos duplicados nela.
    :param t: lista
    :return: boolean
    """
    for i in range(len(t)):
        if t[i] in t[i+1:]:
            return True
    return False


def main():
    t1 = [1,2,3,3]
    t2 = [1,2,3,4]
    t3 = [1,1,2,3]
    print(has_duplicates(t1))
    print(has_duplicates(t2))
    print(has_duplicates(t3))


if __name__ == '__main__':
    main()
