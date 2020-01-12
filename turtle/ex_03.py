def polygon(t, length, n):
    t.color('black', 'red')
    t.begin_fill()
    for c in range(n):
        t.fd(length)
        t.lt(360/n) 
    t.end_fill()


def main():
    import turtle


    t = turtle.Turtle()
    length = 100
    n = 6

    polygon(t, length, n)
    turtle.done()


if __name__ == '__main__':
    main()
