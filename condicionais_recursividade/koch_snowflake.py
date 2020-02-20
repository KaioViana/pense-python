def koch(t, length):
    """Curva de koch nível 1
    :param t: objeto turtle
    :param length: comprimento da curva
    :return: None
    """
    if length < 3:
        t.fd(length)
        return
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)
    t.rt(120)
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)


def koch2(t, length):
    """Curva de koch nível 2
    :param t: objeto turtle
    :param length: comprimento da curva
    :return: None
    """
    koch(t, length/3)
    t.lt(60)
    koch(t,length/3)
    t.rt(120)
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)


def koch3(t, length):
    """Curva de koch nível 3
    :param t: objeto turtle
    :param length: comprimento da curva
    :return: None
    """
    koch2(t, length/3)
    t.lt(60)
    koch2(t,length/3)
    t.rt(120)
    koch2(t, length/3)
    t.lt(60)
    koch2(t, length/3)


def snowflake(t, length):
    """Utiliza a curva de koch nível 3 para desenhar um floco de neve através da recursividade
    :param t: objeto turtle
    :param length: comprimento da curva
    :return: função snowflake, None
    """
    t.color('skyblue', 'skyblue')
    t.speed(10)
    koch3(t, length/3)
    t.lt(60)
    koch3(t,length/3)
    t.rt(120)
    koch3(t, length/3)
    t.lt(60)
    koch3(t, length/3)
    t.rt(120)
    if abs(t.pos()) < 1:
        return
    return snowflake(t, length)
   

def main():
    import turtle


    t = turtle.Turtle() # objeto turtle
    length = 300 # comprimento da curva
    t.begin_fill() # início do desenho
    snowflake(t, length)
    t.end_fill() # fim
    turtle.done() # concluído


if __name__ == '__main__':
    main()
