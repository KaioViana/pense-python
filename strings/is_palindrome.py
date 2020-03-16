def is_palindrome(text):
    if text == text[::-1]:
        return True
    return False


def main():
    text = 'reviver'
    if is_palindrome(text):
        print('Is palindrome')
    else:
        print('Not is palindrome')


if __name__ == '__main__':
    main()
