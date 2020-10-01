"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_equation = input("Please enter your prefix notation equation: ")
    tokens = user_equation.split(' ')

    # if the user input is q then quit
    if user_equation == "q":
        break

    # else run appropriate mathematical operation
    else:

        # if addition
        if tokens[0] == "+":
            print(add(int(tokens[1]), int(tokens[2])))

        # if subtraction
        if tokens[0] == "-":
            print(subtract(int(tokens[1]), int(tokens[2])))
                 
        # if multiplication
        if tokens[0] == "*":
            print(multiply(int(tokens[1]), int(tokens[2])))

        # if division
        if tokens[0] == "/":
            print(divide(int(tokens[1]), int(tokens[2])))

        # if square
        if tokens[0] == 'square':
            print(square(int(tokens[1])))

        # if cube
        if tokens[0] == "cube":
            print(cube(int(tokens[1])))

        # if power
        if tokens[0] == "pow":
            print(power(int(tokens[1]), int(tokens[2])))

        # if mod
        if tokens[0] == "mod":
            print(mod(int(tokens[1]), int(tokens[2])))
