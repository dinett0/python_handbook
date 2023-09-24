class Fraction:
    def __init__(self, n=None, d=None) -> None:
        if isinstance(n, str):
            n, d = int(n.split("/")[0]), int(n.split("/")[1])
        self.numer = n // self.__gcd(n, d)
        self.denom = d // self.__gcd(n, d)

    def numerator(self, number=None):
        if not number:
            return self.numer
        self.numer = number // self.__gcd(number, self.denom)
        self.denom //= self.__gcd(number, self.denom)

    def denominator(self, number=None):
        if not number:
            return self.denom
        self.denom = number // self.__gcd(number, self.numer)
        self.numer //= self.__gcd(number, self.numer)

    def __str__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __repr__(self) -> str:
        return f"Fraction({self.numer}, {self.denom})"

    def __gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.__gcd(b, a % b)

    def __add__(self, other):
        return Fraction(
            self.numer + other.numerator(), self.denom + other.denominator()
        )

    def __sub__(self, other):
        return Fraction(
            self.numer - other.numerator(), self.denom - other.denominator()
        )

    def __iadd__(self, other):
        if self.denom != other.denominator():
            gcd = self.__gcd(self.denom, other.denominator())
            if gcd == 1:
                self.denom *= other.denominator()
                self.numer *= other.denominator()
                other.numerator(self.denom)
                other.denominator(self.denom)
            else:
                min() * gcd
        self.number += other.numerator()
        self.denom += other.denominator()
        return self

    def __isub__(self, other):
        self.number -= other.numerator()
        self.denom -= other.denominator()
        return self


a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)
