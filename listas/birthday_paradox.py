def random_bdays(n):
    """Gera uma lista contendo dias de aniversários aleatórios.

    :param n: quantidade de elementos

    :var t: lista
    :var bday: dia do ano

    :return: boolean
    """
    from random import randint

    t = []
    for i in range(n):
        bday = randint(1, 365)
        t.append(bday)
    return t


def count_macthes(num_students, num_simulations):
    """Conta o número de colisões de aniversários no mesmo dia de acordo com as simulações.

    :param num_students: número de estudantes
    :param num_simulations: número de simulações

    :var count: contador
    :var t: lista com dias de aniversário no ano

    :return: número de colisões
    """
    from has_duplicates import has_duplicates

    count = 0

    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    num_students = 23
    num_simulations = 1000
    num_matches = count_macthes(num_students, num_simulations)

    print(f'Em uma sala com {num_students}, depois de {num_simulations} simulação(es), foi obtido {num_matches} colisões.')


if __name__ == '__main__':
    main()
