class FractionCalculator:
    def __init__(self):

        self.num1_numerator = 0
        self.num2_numerator = 0
        self.num1_denominator = 0
        self.num2_denominator = 0
        self.whole_num = None
        self.numerator = None
        self.denominator = None
        self.result = None
        self.lcm = 0  # Lowest common multiple
        self.gcd = 0  # Greatest common divisor
        self.is_negative = False

    def calculate(self, num1, num2, operator):
        self.num1_numerator = num1.get_numerator()
        self.num1_denominator = num1.get_denominator()
        self.num2_numerator = num2.get_numerator()
        self.num2_denominator = num2.get_denominator()

        valid_operators = ['+', '-', '*', '/']
        if operator not in valid_operators:
            print('Please enter a valid operator next time.')
            exit()

        if operator == "+":
            self.addition()

        if operator == "-":
           self.subtraction()


        if operator == "*":
            self.multiplication()

        if operator == "/":
            self.division()

        self.simplify()

        self.print_results()

    def addition(self):
        # Calls lowestCommonMultiple to convert the fraction then adds them and calls simplify
        if self.num1_denominator != self.num2_denominator:
            self.lowest_common_multiple()
            self.numerator = self.num1_numerator + self.num2_numerator
            self.denominator = self.lcm

        # Performs addition and calls simplify if the denominators are already the same
        else:
            self.numerator = self.num1_numerator + self.num2_numerator
            self.denominator = self.num1_denominator

    def subtraction(self):
        # Calls lowestCommonMultiple to convert the fraction then subtracts them and calls simplify
        if self.num1_denominator != self.num2_denominator:

            self.lowest_common_multiple()
            self.numerator = self.num1_numerator - self.num2_numerator
            self.denominator = self.lcm

        # Performs subtraction and calls simplify if the denominators are already the same
        else:
            self.numerator = self.num1_numerator - self.num2_numerator
            self.denominator = self.num1_denominator

    def multiplication(self):
        # Performs multiplicaton then reduces with simplify
        self.numerator = self.num1_numerator * self.num2_numerator
        self.denominator = self.num1_denominator * self.num2_denominator

    def division(self):
        # Performs division then reduces with simplify
        self.numerator = self.num1_numerator * self.num2_denominator
        self.denominator = self.num1_denominator * self.num2_numerator

    def lowest_common_multiple(self):
        # Finds the greatest common divisor
        self.greatest_common_divisor(self.num1_denominator, self.num2_denominator)

        # Finds the least common multiple using the greatest common divisor
        self.lcm = (self.num1_denominator * self.num2_denominator) / self.gcd

        # Sets both denominators to the lcm and multiplies numerators accordingly
        if self.num1_denominator != self.lcm:
            x = self.lcm / self.num1_denominator
            self.num1_numerator = self.num1_numerator * x
            self.num1_denominator = self.lcm
        if self.num2_denominator != self.lcm:
            x = self.lcm / self.num2_denominator
            self.num2_numerator = self.num2_numerator * x
            self.denominator = self.lcm

    # I wrote my own function here, but there is a built in gcd method in python
    def greatest_common_divisor(self, first_num, second_num):
        # Finds the greatest common divisor using the Euclidean algorithm
        if first_num > second_num:
            x = first_num
            y = second_num
        else:
            x = second_num
            y = first_num
        while x % y != 0:
            temp = x % y
            x = y
            y = temp
            self.gcd = temp
        if x % y == 0:
            self.gcd = abs(y)

    def simplify(self):

        self.greatest_common_divisor(self.numerator, self.denominator)

        if (self.numerator < 0) is not (self.denominator < 0):
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)
            self.is_negative = True

        if self.numerator < 0 and self.denominator < 0:
            self.numerator = abs(self.numerator)
            self.denominator = abs(self.denominator)
            self.is_negative = False

        # Converts improper fraction to a mixed number if necessary
        if self.numerator > self.denominator:
            self.whole_num = self.numerator // self.denominator
            self.numerator = self.numerator % self.denominator
            self.numerator = self.numerator / self.gcd
            self.denominator = self.denominator / self.gcd

        else:
            self.numerator = self.numerator / self.gcd
            self.denominator = self.denominator / self.gcd
            if self.numerator == self.denominator:
                self.whole_num = 1
                self.numerator = None
                self.denominator = None

    def print_results(self):

        if self.whole_num:
            self.whole_num = int(self.whole_num)
        if self.numerator:
            self.numerator = int(self.numerator)
        if self.denominator:
            self.denominator = int(self.denominator)
        if self.is_negative == True:
            self.result = '-'

        else:
            self.result = ''

        if self.whole_num:
            self.result = self.result + str(self.whole_num)
            if self.numerator:
                self.result = self.result + "_" + (str(self.numerator)) + '/' + str(self.denominator)
            print('The solution is: ' + self.result)
        else:
            self.result = self.result + str(self.numerator) + "/" + str(self.denominator)
            print('The solution is: ' + self.result)

    # Getter functions
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_whole_num(self):
        return self.whole_num

    def get_lcm(self):
        return self.lcm

    def get_gcd(self):
        return self.gcd

    def get_result(self):
        return self.result

    def get_is_negative(self):
        return self.is_negative