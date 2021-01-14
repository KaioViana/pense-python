import dbm
from unidecode import unidecode


def anagram_set(file):
    anagrams_map = {}
    d = {}

    anagrams_file = open('anagrams_file', 'w')

    words = list(set(open(file, 'r').read().split()))
    words.sort()

    for word in words:
        sorted_word = ''.join(sorted(unidecode(word.lower())))
        d.setdefault(sorted_word, []).append(word)
    [anagrams_map.setdefault(d[k][0], []).extend(d[k]) for k in d if len(d[k]) >= 1]

    for k in anagrams_map:
        anagrams_file.write(f'WORD:::: {k} MAP:::: {anagrams_map[k][1:]}\n')
        
    return anagrams_map


def store_anagrams(db, dic):
    for k, v in dic.items():
        db[k] = str(v)


def read_anagrams(db, word):
    try:
        return db[word][1:-1].decode('utf-8')

    except:
        raise KeyError('Chave não encontrada')


def main():
    db = dbm.open('anagrams_data', 'c')
    anagrams_map = anagram_set('palavras_ptbr')

    store_anagrams(db, anagrams_map)

    print('='*10, 'ANAGRAMS FINDER', '='*10, end='\n')
    while True:

        user = str(input('Informe uma palavra a ser buscada no banco (digite sair para finalizar): ')).strip()
        if user == 'sair':
            db.close()
            break
        else:
            try:
                search = read_anagrams(db, user)
                print('Anagramas:', search)
            except KeyError as err:
                print(err)
        print()
                

if __name__ == '__main__':
    main()
