import fraction
import fractionCalculator

def main():

    print('Welcome to my Fraction Calculator!\n')
    equation = input('Please enter an equation:')
    equation = equation.split()

    # Create a fraction object for the first number in the equation and parse it
    fraction1 = fraction.Fraction(equation[0])

    # Create a fraction object for the second number in the equation and parse it
    fraction2 = fraction.Fraction(equation[2])

    # Calculate and print the solution
    calculator = fractionCalculator.FractionCalculator()
    print('The solution is:')
    calculator.calculate(fraction1, fraction2, equation[1])


if __name__ == "__main__":
    main()