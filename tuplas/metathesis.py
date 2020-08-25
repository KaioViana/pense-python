def metathesis(word1, word2):
    """Recebe duas palavras e verifica se elas formam um par de metátese.
        :param word1, word2: palavras a serem analizadas.
        :var ziped: lista zipada de word1 e word2.
        :var pos: contador de posição na lista.
        :return: boolean.
    """
    ziped = list(zip(word1, word2))
    pos = 0
    for x, y in ziped:
        if x != y:
            w1 = list(word1)
            w2 = list(word2)

            w2[pos], w2[pos+3] = w2[pos+3], w2[pos]

            if w1 == w2:
                return True
            return False
        pos += 1


def main():
    word1 = 'conserve'
    word2 = 'converse'

    print(metathesis(word1, word2))


if __name__ == '__main__':
    main()
