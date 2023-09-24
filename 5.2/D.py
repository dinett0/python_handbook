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


fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
