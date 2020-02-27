def ack(m, n):
    # "guardiões"
    if not isinstance(n, int) or not isinstance(m, int):
        raise 'Esta função aceita apenas valores inteiros'
    if n < 0 or m < 0:
        raise 'Esta função aceita apenas valores positivos'


    # função de Ackermann
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


def main():
    import sys
    from random import randint
    

    sys.setrecursionlimit(1000000000) # definindo limite máximo de recursividade

    m,n = (randint(0, 5), randint(0, 5))
    f = ack(m, n)
    print(f)


if __name__ == '__main__':
    main()
