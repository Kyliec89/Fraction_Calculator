import fraction
import fractionCalculator


def main():
    user_wants_to_continue = True

    while user_wants_to_continue:

        equation = input('Please enter an equation:')
        equation = equation.split()

        if len(equation) != 3:
            print("Invalid input, please try again.")
            main()

        # Create a fraction object for the first number in the equation and parse it
        fraction1 = fraction.Fraction()
        fraction1.parser(equation[0])

        # Create a fraction object for the second number in the equation and parse it
        fraction2 = fraction.Fraction()
        fraction2.parser(equation[2])

        # Calculate and print the solution
        calculator = fractionCalculator.FractionCalculator()
        calculator.calculate(fraction1, fraction2, equation[1])

        print('Do you want to enter another equation?')

        continue_prompt = input('Please enter Y to continue, or Q to quit.')

        if continue_prompt.upper() == 'Y':
            user_wants_to_continue = True
        if continue_prompt.upper() == 'Q':
            user_wants_to_continue = False


if __name__ == "__main__":
    print('Welcome to my Fraction Calculator!\n')
    main()
