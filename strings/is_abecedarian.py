def is_abecedarian(word):
    """Verifica se as letras de uma palavra está em ordem alfabética
    :param word: palavra a ser verificada
    :return: boolean
    """
    if len(word) <= 1:
        return True

    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])


def main():
    # lendo words.txt
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip().lower()
            if is_abecedarian(word):
                print(word)


if __name__ == '__main__':
    main()
