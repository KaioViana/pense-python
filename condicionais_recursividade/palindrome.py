def is_palindrome(s):
    """Verifica se uma palavra é um palíndromo.
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


if __name__ == '__main__':
    main()
