def square(t, length):
    t.begin_fill()
    for c in range(4):
        t.fd(length)
        t.lt(90)
    t.end_fill()


def main():
    import turtle


    t = turtle.Turtle()
    l = 300
    square(t, l)
    turtle.done()



if __name__ == '__main__':
    main()
