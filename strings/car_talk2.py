def has_palindrome(string):
    """Recebe uma string e verifica se em algum lugar dela há um palíndromo.
    :param string: string a ser analizada
    :var string2: variável onde pode conter o possível palíndromo
    :return: boolean"""
    from is_palindrome import is_palindrome


    for i in range(len(string)):
        string2 = string[i+1:]
        for j in range(len(string2)):
            if string[i] == string2[j]:
                if is_palindrome(string[i]+string2[:j+1]):
                    return True
    return False


def main():
    from random import randint


    # girando todos os valores de 6 dígitos
    for i in range(100000, 1000000):
        s = str(i)
        # verificando se há palíndromo no dígito
        if has_palindrome(s):
            print(s)



if __name__ == '__main__':
    main()