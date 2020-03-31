def only_twenty(word):
    """Verifica se uma palavra contêm somente 20 caracteres
    
        :param word: palavra a ser verificada
        :return: boolean
    """
    if len(word) > 20:
        return True
    return False


def main():
    with open('words.txt', 'r') as arq:
        for line in arq:
            word = line.strip()
            if only_twenty(word):
                print(word.upper())


if __name__ == '__main__':
    main()
