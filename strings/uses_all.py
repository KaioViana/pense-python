def uses_all(word, letters):
    """Usa uses_only para verficar se determinada palavra contêm determinada sequência de letras
    :param word: palavra a ser analizada
    :param letters: sequência de letras
    :return: boolean
    """
    from uses_only import uses_only


    return uses_only(letters, word)


def main():
    # lendo words.txt
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip().lower()
            if uses_all(word, 'aeiouyd'):
                print(word)


if __name__ == '__main__':
    main()
     