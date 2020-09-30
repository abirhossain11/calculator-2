"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_equation = input("Please enter your prefix notation equation: ")
    print(user_equation)
    token_input = user_equation.split(' ')
    print(token_input)
    break
