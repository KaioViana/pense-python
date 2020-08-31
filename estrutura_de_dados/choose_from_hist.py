def histogram(seq):
    """Recebe uma sequência e retorna um histograma dessa sequência
        :param seq: sequência a ser trabalhada
        :var d: dicionário contendo o histograma
        :return: histograma
    """
    d = dict()

    for letter in seq:
        d[letter] = d.get(letter, 0) + 1
    print(d)
    return d


def choose_from_hist(hist):
    """Escolhe aleatoriamente um valor em um histograma
       e retorna sua probabilidade em proporção à frequência.
        :param d: histograma a ser trabalhado
        :var t: tupla contendo chave/valor da escolha aleatória no histograma
        :var max_length: frequência máxima
        :return: probabilidade em proporção à frequência
    """
    from random import choice


    t = choice(list(hist.items()))
    max_length = sum(hist.values())

    return f'{t[0]} com probabilidade {t[1]}/{max_length} -> {(t[1]/max_length) * 100:.2f} %' 


def main():
    seq = 'aab'
    d = histogram(seq)
    print(choose_from_hist(d))


if __name__ == '__main__':
    main()