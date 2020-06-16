def invert_dict(d):
    inverse = dict()

    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse


def main():
    msg = 'parrot'
    d = dict()

    for letter in msg:
        d[letter] = d.get(letter, 0) + 1

    inverse = invert_dict(d)

    print(d)
    print(inverse)


if __name__ == '__main__':
    main()
