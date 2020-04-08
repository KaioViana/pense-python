def uses_only(word, letters):
    """Recebe uma palavra e uma sequência de letras e verica se a palavra contêm somente as letras da sequência
    :param word: palavra a ser analizada
    :param letters: sequência de letras
    :return: boolean
    """
    for letter in word:
        if letter not in letters:
            return False
    return True


def main():
    from time import sleep


    user_letters = str(input('INFORME UMA SEQUÊNCIA DE LETRAS:\n')).strip().lower()
    print('='*15)
    print('ANALIZANDO...')
    print('='*15)

    sleep(3)

    # lendo o arquivo words.txt
    with open('words.txt') as fin:
        for line in fin:
            word = line.strip()
            if uses_only(word, user_letters):
                print(word)          


if __name__ == '__main__':
    main()
