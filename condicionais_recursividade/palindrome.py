def is_palindrome(s):
<<<<<<< HEAD
    """Verifica se uma palavra é um palíndromo.
=======
<<<<<<< HEAD
    """Verifica se uma palavra é um palíndromo.
=======
    """Verifica se uma palavra é um palídromo.
>>>>>>> f28b2bfb8b75a3de517d12d414e4e58adc56b8d1
>>>>>>> d9646dfbf3549ab57718029239d2fdad9fba8553
    :param s: palavra
    :return: boolean
    """
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else: return False


def main():
    try:
        s = str(input('Informe uma palavra: ')).strip()
        print(is_palindrome(s))
    except Exception as error:
        print('Exceção encontrada:', error)

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
 
>>>>>>> f28b2bfb8b75a3de517d12d414e4e58adc56b8d1
>>>>>>> d9646dfbf3549ab57718029239d2fdad9fba8553
if __name__ == '__main__':
    main()
