def is_sorted(t):
    """Recebe uma lista e verifica se ela está em ordem ascendente
    
    :param t: lista
    :return: boolean
    """
    if t == sorted(t):
        return True
    return False


def main():
    t1 = [1,2,3]
    t2 = ['b', 'a']
    print('t1:', is_sorted(t1), '\nt2:', is_sorted(t2))


if __name__ == '__main__':
    main()
