def chop(t):
    """Recebe uma lista e remove o primeiro e último elemento dela
    
    :param t: lista
    :return: None
    """
    del t[0]
    del t[-1]
    return None


def main():
    t = [1,2,3,4]
    chop(t)
    print(t)


if __name__ == '__main__':
    main()
