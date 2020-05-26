def list_words_append():
    t = []
    with open('words.txt', 'r') as fin:
        for line in fin.readlines():
            word = line.strip()
            t.append(word)
    return None


def list_words_attribution():
    t = []
    with open('words.txt', 'r') as fin:
        for line in fin.readlines():
            word = line.strip()
            t = t + [word]
    return None  


def main():
    import time
    

    print('Executando método append:')
    start_time = time.time()
    list_words_append()
    print(f'Tempo de execução: {time.time() - start_time:.2f}')
    print('\nExecutando método de atribuição:')
    start_time = time.time()
    list_words_attribution()
    print(f'Tempo de execução: {time.time() - start_time:.2f}')


if __name__ == '__main__':
    main()
