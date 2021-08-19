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
        if self.imag == 0:
            print(self.real)
        elif self.imag > 0:
            print(f'({self.real}+{self.imag}i)')
        else:
            print(f'({self.real}-{-self.imag}i)')

    def add(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)

    def less(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)


cn1 = ComplexNumber(5, 1)
cn2 = ComplexNumber(2, 3)

cn3 = cn1.add(cn2)
cn3.prettyprint()
cn3 = cn1.less(cn2)
cn3.prettyprint()
