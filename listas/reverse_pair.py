def reverse_pair(t, word):
    """Utiliza-se da busca binária para encontrar o par inverso de uma palavra.
    Recebe uma lista de palavras e a palavra a ser analizada.
    
    :param t: lista de palavras
    :param word: palavra a ser analizada
    
    :var search_pos: posição da palavra encontrada na lista
    
    :return: -1 caso não encontre nada ou uma tupla contendo a palavra, seu par inverso e sua posição.
    """
    from in_bisect import in_bisect


    search_pos = in_bisect(t, word[::-1])

    if search_pos == -1:
        return -1
    return (word, t[search_pos], search_pos)


def main():
    """Extrai palavras de um arquivo txt para uma lista e passa cada uma para reverse_pair
    para ser analizada.
    """
    t = []

    with open('words.txt') as fin:
        for line in fin.readlines():
            word = line.strip()
            t.append(word)
    
    for word in t:
        pair = reverse_pair(t, word)

        if not pair == -1:
            print(pair)


if __name__ == '__main__':
    main()
