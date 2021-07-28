class Fraction:
    def __init__(self):
        self.input_fraction = None
        self.numerator = None
        self.denominator = None
        self.whole_num = None
        self.is_mixed = False

    def parser(self, input_fraction):
        self.input_fraction = input_fraction

        # Converts a whole number to a fraction
        if '_' and '/' not in self.input_fraction:
            self.validity_error(self.input_fraction)
            self.numerator = int(self.input_fraction)
            self.denominator = 1

        # Parses the number if mixed
        if '_' in self.input_fraction:
            whole_num_split = self.input_fraction.split('_')
            self.validity_error(whole_num_split[0])
            self.whole_num = int(whole_num_split[0])
            fraction = whole_num_split[1]
            fraction = fraction.split('/')
            self.validity_error(fraction[0])
            self.validity_error(fraction[1])
            self.numerator = int(fraction[0])
            self.denominator = int(fraction[1])
            self.is_mixed = True

        # Parses the number if a plain fraction
        if '/' in self.input_fraction and '_' not in self.input_fraction:
            fraction = self.input_fraction.split('/')
            self.validity_error(fraction[0])
            self.validity_error(fraction[1])
            self.numerator = int(fraction[0])
            self.denominator = int(fraction[1])

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

    # If a fraction is mixed, make it improper
    def convert_to_improper(self):
        if self.is_mixed == True:
            self.numerator = (self.whole_num * self.denominator) + self.numerator

    # Error message for fractions with a 0 denominator
    def zero_error(self):
        if self.denominator == 0:
            print("A fraction with a 0 denominator is undefined, please enter a legal fraction next time!")
            exit()
        else:
            pass

    def validity_error(self, num):
        num = num.lstrip('-')
        valid_check = num.isnumeric()
        if not valid_check:
            print('Please enter a valid fraction, whole number, or mixed number next time.')
            exit()
        else:
            pass

    # Getter functions
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_is_mixed(self):
        return self.is_mixed

