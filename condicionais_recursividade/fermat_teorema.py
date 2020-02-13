def check_fermat(a=0, b=0, c=0, n=0, conj=set(), tentativas=5454):
    """Tenta resolver o teorema de Fermat atravês da recursividade. Se for resolvido imprime uma mensagem
    dizendo que o impossível aconteceu XD. Caso não, ele tenta a quantidade de vezes informada.

    :param a: valor cateto
    :param b: valor cateto
    :param c: valor hipotenusa
    :param n: valor do expoente
    :param conj: estrutura de dados do tipo set
    :param tentativas: número de tentativas
    :return: None
    """
    from random import randint


    print('tentativas:', tentativas, 'comprimento do conjunto:', len(conj))

    if tentativas == 0:
        print(str('Máximo de tentativas atingido!').upper())
        return None

    a = randint(1, 10000)
    b = randint(1, 10000)
    c = randint(1, 10000)
    n = randint(1, 10000)

    tupl = (a,b,c,n)
    
    print(f'\nCÁLCULO:\nAB: {(a**2) + (b**2)} ==> C:{c**2}')
    print('IGUALDADE: ', (a**n) + (b**n) == c**n, '\n')

    if (a**n) + (b**n) == c**n and n > 2:
        print(str('Holy Smokes, Fermat was wrong!').upper())
        return None
    else:
        conj.update([tupl])

        while tupl in conj:
            a = randint(1, 10000)
            b = randint(1, 10000)
            c = randint(1, 10000)
            n = randint(1, 10000)

            tupl = (a,b,c,n)

            
        #input(str(f'Tupla {tupl} não contém no conjunto. ENTER para continuar: \n'))

        a = tupl[0]
        b = tupl[1]
        c = tupl[2]
        n = tupl[3]
        
        check_fermat(a, b, c, n, conj, (tentativas - 1))


def main():
    import sys
    sys.setrecursionlimit(1000000000)
    check_fermat()


if __name__ == '__main__':
    help(check_fermat)
