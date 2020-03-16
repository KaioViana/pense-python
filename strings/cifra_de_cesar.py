def rotate_word(word, r=0):
    """Utiliza a Cifra de César para criptografar palavres
    :param word: palavra a ser criptografada
    :parama r: quantidade de casas a ser rotacionada
    :return: palavra criptografada"""
    from functools import reduce
    start = ord('a')
    new_word = ''
    vector = []

    for letter in word.lower():
        vector.append((ord(letter) - start) + (r))
    
    for i in vector:
        i = (i % 26) + start
        new_word += chr(i)
    
    return new_word


def main():
    word='cheer'
    rotate = rotate_word(word, 7)
    print(rotate)


if __name__ == '__main__':
    main()
