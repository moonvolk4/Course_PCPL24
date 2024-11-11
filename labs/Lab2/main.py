from lab_python_oop.rectangle import rectangle
from lab_python_oop.circle import circle
from lab_python_oop.square import square


def main():
    N = 5

    Rectangle = rectangle(N, N, "синего")
    Circle = circle(N, "зеленого")
    Square = square(N, "красного")

    print(Rectangle)
    print(Circle)
    print(Square)


if __name__ == "__main__":
    main()
