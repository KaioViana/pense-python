def alterned_word(word_1, word_2):
    alterned = ''
    zipped = list(zip(word_1, word_2))

    for t in zipped:
        alterned += t[0] + t[1]
    return alterned


def main():
    word_1 = 'shoe'
    word_2 = 'cold'

    print(alterned_word(word_1, word_2))


if __name__ == '__main__':
    main()
