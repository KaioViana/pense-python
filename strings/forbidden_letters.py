def avoids(word, letters):
    """Recebe uma palavra e um quantidade de letras proíbidas e verifica se a palavras às contêm
    :param word: palavra a ser analisada
    :param letters: letras proíbidas
    :return: boolean
    """
    for letter in word:
        if letter in letters:
            return False
    return True
        


def main():
    from time import sleep

    while True:
        user_word = str(input('INFORME UMA PALAVRA:\n')).upper().strip()
        user_letters = str(input('INFORME AS LETRAS PROÍBIDAS:\n')).upper().strip()

        print('='*21)
        print('PROCESSANDO...')
        sleep(1)
        print('='*21)

        if avoids(user_word, user_letters):
            print('PASSOU NA VERIFICAÇÃO!')
        else:
            print('CONTÊM LETRAS PROÍBIDAS!')
        print('='*21)
        flag = str(input('DESEJA CONTINUAR ? (S/N)\n')).upper().strip()

        while flag != 'S' and flag != 'N':
            flag = str(input('COMANDO NÃO ENTENDIDO. INFORME NOVAMENTE: (S/N)\n')).upper().strip()
        
        if flag == 'N':
            break
        print('='*21)

if __name__ == '__main__':
    main()
