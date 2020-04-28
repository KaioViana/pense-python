def is_anagram(word1, word2):
    """Recebe duas strings e verifica se são anagramas
    
    :param word1: primeira string
    :param word2: segunda string
    :return: boolean
    """
    word1 = word1.upper()
    word2 = word2.upper()
    if len(word1) >= len(word2):
        for letter in word2:
            if letter not in word1:
                return False
    else:
        for letter in word1:
            if letter not in word2:
                return False
    return True


def main():
    word1 = 'lasca'
    word2 = 'aaicsl'
    print(is_anagram(word1, word2))


if __name__ == '__main__':
    main()
