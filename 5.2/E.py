class Fraction:
    def __init__(self, n=None, d=None) -> None:
        if isinstance(n, str):
            n, d = int(n.split("/")[0]), int(n.split("/")[1])
        self.numer = n // self.__gcd(n, d)
        self.denom = d // self.__gcd(n, d)
        self.__normalise_sign()

    def numerator(self, number=None):
        if number:
            self.numer = number // self.__gcd(number, self.denom)
            self.denom //= self.__gcd(number, self.denom)
            self.__normalise_sign()
        return abs(self.numer)

    def denominator(self, number=None):
        if number:
            self.denom = number // self.__gcd(number, self.numer)
            self.numer //= self.__gcd(number, self.numer)
            self.__normalise_sign()
        return abs(self.denom)

    def __str__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __repr__(self) -> str:
        return f"Fraction('{self.numer}/{self.denom}')"

    def __neg__(self):
        return Fraction(self.numer, -self.denom)

    def __normalise_sign(self):
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    def __gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.__gcd(b, a % b)


f = Fraction(10, -3)
print(f)
