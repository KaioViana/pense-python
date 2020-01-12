def square(t):
    t.begin_fill()
    for c in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()


def main():
    import turtle


    t = turtle.Turtle()
    square(t)
    turtle.done()



if __name__ == '__main__':
    main()
