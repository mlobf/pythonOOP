class ComplexNumber:
    """
        Using a + operator by __methods
    """

    def __init__(self, real: int = 0.0, imag: int = 0.0):
        self.real = real
        self.imag = imag

    def prettyprint(self):
        """
            Just a print method
        """
        if self.imag == 0:
            print(self.real)
        elif self.imag > 0:
            print(f"({self.real}+{self.imag}i)")
        else:
            print(f"({self.real}-{-self.imag}i)")

    def __add__(self, other: int = 0.0):
        """
            To add imaginary number to other
        """
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)

    def __less__(self, other: int = 0.0):
        """
            To less imaginary number to other
        """
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)


cn0 = ComplexNumber(5, 3)
cn1 = ComplexNumber(2, 1)
c = cn0 + cn1
c.prettyprint()


c = cn0 - cn1
c.prettyprint()
