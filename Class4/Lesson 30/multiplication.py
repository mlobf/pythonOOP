class ComplexNumber:
    """
    this is an abstration.
    How to models a oop in python to
    create a complex number
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

    def __sub__(self, other: int = 0.0):
        """
            To subtract imaginary number to other
        """
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)

    def __mul__(self, other: int = 0.0):
        """
            To mulplication imaginary number to other
        """
        r = self.real * other.real - self.imag*other.imag
        i = self.real * other.imag + self.imag*other.real
        return ComplexNumber(r, i)


cn1 = ComplexNumber(5, 3)
cn2 = ComplexNumber(2, 6)

cn3 = cn1 * cn2
cn3.prettyprint()
