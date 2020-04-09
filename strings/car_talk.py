def consecutive_letters(word):
    consecutive = 0
    i = 0

    while i < len(word)-1:
        if word[i] == word[i+1]:
            consecutive += 1
            i += 1
        else:
            consecutive = 0
        
        if consecutive == 3:
            return True
        i += 1
    return False


def main():
    # lendo words.txt
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip().lower()
            if consecutive_letters(word):
                print(word)


if __name__ == '__main__':
    main()
