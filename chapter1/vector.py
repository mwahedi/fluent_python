from math import hypot


# using type hinting
class Vector:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # using %r to use the new Format String Syntax (http://bit.ly/1Vm7gD1)
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self) -> float:
        return hypot(self.x, self.y)

    def __bool__(self) -> float:
        return bool(abs(self))

    def __add__(self, other: 'Vector') -> 'Vector':
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    print(f'v1 + v2 = {v1 + v2}')

    v = Vector(3, 4)
    print(f"new vector v = {v}")
    print(f"absolute value of integers and floats is: {abs(v)}")

    print(f"what does the bool function do: {bool(v)}")
