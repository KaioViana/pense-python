from turtle import *


def flower1():
    speed(10)
    color('red', 'yellow')

    begin_fill()
    while True:
        circle(100, 150)
        lt(100)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


def main():
    flower1()


if __name__ == '__main__':
    main()
