def check_fermat(a=1, b=1, c=1, n=1, conj=set(), tentativas=50000):
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
    from time import sleep


    print('tentativas:', tentativas, 'comprimento do conjunto:', len(conj))

    if tentativas == 0:
        print(str('Máximo de tentativas atingido!').upper())
        return None

    tupl = tuple()
    
    print(f'\nCÁLCULO:\nValor de n: {n}\nAB: {(a**2) + (b**2)} ==> C:{c**2}')
    print('IGUALDADE: ', (a**n) + (b**n) == c**n, '\n')

    if (a**n) + (b**n) == c**n and n > 2:
        print(str('Holy Smokes, Fermat was wrong!').upper())
        return None
    else:
        tupl = (a,b,c,n)
        conj.update([tupl])

        while tupl in conj:
            if len(conj) == 100**4:
                print('\nCombinações maxímas atingidas', len(conj))
                return None
            a = randint(1, 100)
            b = randint(1, 100)
            c = randint(1, 100)
            n = randint(1, 100)

            tupl = (a,b,c,n)

            
        #input(str(f'Tupla {tupl} não contém no conjunto. ENTER para continuar: \n'))
        conj.update([tupl])
        a = tupl[0]
        b = tupl[1]
        c = tupl[2]
        n = tupl[3]
        
        sleep(0.05)
        return check_fermat(a, b, c, n, conj, (tentativas - 1))


def main():
    import sys
    sys.setrecursionlimit(1000000000)
    check_fermat()


if __name__ == '__main__':
    main()
