def in_bisect(t, item):
    """Utiliza-se da busca binária para encontrar a posição de um elemento.

    :param t: lista
    :param item: item a ser procurado na lista
    
    :var first: primeira posição da lista
    :var last: última posição da lista
    :var middle: posição do meio da lista

    :return: -1 caso não encontre ou middle caso encontre
    """
    first = 0
    last = len(t) - 1

    while first <= last:
        middle = (first + last)//2
        if item == t[middle]:
            return middle
        else:
            if item < t[middle]:
                last = middle - 1
            elif item > t[middle]:
                first = middle + 1
    return -1


def in_bisect_recursive(t, item, first, last):
    """Utiliza-se da busca binária recursiva para encontrar a posição de um elemento.

    :param t: lista
    :param item: item a ser procurado na lista
    :param first: primeira posição da lista
    :param last: última posição da lista

    :var middle: posição do meio da lista

    :return: -1 caso não encontre o elemento ou middle caso encontre
    """
    if first > last:
        return -1
    
    middle = (first + last)//2

    if item == t[middle]:
        return middle
    else:
        if item < t[middle]:
            return in_bisect_recursive(t, item, first, middle-1)
        elif item > t[middle]:
            return in_bisect_recursive(t, item, middle+1, last)


def main():
    from time import time


    t = [] # lista para armazenamento

    # lendo arquivo de palavras
    with open('words.txt') as fin:
        for line in fin.readlines():
            word = line.strip()
            t.append(word)
              
    print(f'EXECUTANDO BUSCA BINÁRIA NORMAL>>>')
    time_start = time()
    print(in_bisect(t, 'trivia'))
    print(f'BUSCA EXECUTADA EM {time()-time_start}')
    print(f'\nEXECUTANDO BUSCA BINÁRIA RECURSIVA>>>')
    time_start = time()
    print(in_bisect_recursive(t, 'welcome', 0, len(t)-1))
    print(f'BUSCA EXECUTADA EM {time()-time_start}')


if __name__ == '__main__':
    main()
