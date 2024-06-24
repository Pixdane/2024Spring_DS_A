#27653: Fraction类
import math

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ZeroDivisionError
        g = math.gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __add__(self, other):
        numerator = self.numerator*other.denominator + self.denominator*other.numerator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

a, b, c, d = map(int, input().split())
print(Fraction(a, b) + Fraction(c, d))
