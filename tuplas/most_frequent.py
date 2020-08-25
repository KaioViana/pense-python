def histogram(word):
    """Recebe uma palavra e retorna um dicionário de frequência de letras.
        :param word: palavra a ser analizada.
        :var freq: dicionário de frequência de letras na palavra.
        :return: dict.
    """
    freq = dict()

    for letter in word:
        freq[letter] = freq.get(letter, 0) + 1

    return freq


def most_frequent(word):
    """Recebe uma palavra, verifica sua frequência e cria uma nova string da frequência
       de letras em ordem decrescente.
        :param word: palavra a ser analizada.
        :var t: lista de tuplas contendo a letra e sua respectiva frequência.
        :var res: lista contendo os valores da nova string
        :var hist: dicionário de frequências de letras da palavra.
        :return: string.
    """
    t = list()
    res = list()
    hist = histogram(word)

    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    for freq, x in t:
        res.append(x*freq)
    
    return ''.join(res)


def main():
    word = 'parrot'

    print(most_frequent(word))


if __name__ == '__main__':
    main()
