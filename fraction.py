class Fraction:
    def __init__(self, input_fraction):
        self.input_fraction = str(input_fraction)
        self.numerator = None
        self.denominator = None
        self.whole_num = None
        self.is_mixed = False

        if '_' and '/' not in self.input_fraction:
            self.numerator = int(self.input_fraction)
            self.denominator = 1

        # Parses the first number if mixed
        if '_' in self.input_fraction:
            self.input_fraction = self.input_fraction.split('_')
            self.whole_num = int(self.input_fraction[0])
            fraction = self.input_fraction[1]
            fraction = fraction.split('/')
            self.numerator = int(fraction[0])
            self.denominator = int(fraction[1])
            self.is_mixed = True
        # Parses the first number if a plain fraction
        if '/' in self.input_fraction:
            self.input_fraction = self.input_fraction.split('/')
            self.numerator = int(self.input_fraction[0])
            self.denominator = int(self.input_fraction[1])

        # Moves the negative sign to the whole number if present on fraction in mixed number
        if (self.numerator < 0) or (self.denominator < 0):
            if self.whole_num and self.whole_num > 0:
                self.numerator = abs(self.numerator)
                self.denominator = abs(self.denominator)
                self.whole_num = self.whole_num * -1

        if self.whole_num and self.whole_num < 0:
            self.numerator = self.numerator * -1

        self.zero_error()

        self.convert_to_improper()

    def convert_to_improper(self):
        # If a fraction is mixed, make it improper
        if self.is_mixed == True:
            self.numerator = (self.whole_num * self.denominator) + self.numerator

    def zero_error(self):
        if self.denominator == 0:
            print("A fraction with a 0 denominator is undefined, please enter a legal fraction next time!")
            exit()
        else:
            pass
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_is_mixed(self):
        return self.is_mixed

