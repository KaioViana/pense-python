def has_no_e(word):
    """Verifica se uma dada palavra não contêm a letra "e"

        :param word: palavra a ser verificada
        :var wordLower: variável que contêm a palavra convertida para letras minúsculas
        :return: boolean
    """
    wordLower = word.lower()

    if 'e' not in wordLower:
        return True
    return False


def main():
    counter_no_e = 0
    counter_lines = 0

    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip()
            if  has_no_e(word):
                print(word)
                counter_no_e += 1
            counter_lines += 1
        percent = (counter_no_e/counter_lines)*100
    print(f'{percent:.2f}% das palavras não contêm a letra "e"')


if __name__ == '__main__':
    main()
