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
        if tokens[0] == "+" or tokens[0] == "add":
            print(add(float(tokens[1]), float(tokens[2])))

        # if subtraction
        if tokens[0] == "-" or tokens[0] == "subtract":
            print(subtract(float(tokens[1]), float(tokens[2])))
                 
        # if multiplication
        if tokens[0] == "*" or tokens[0] == "multiply":
            print(multiply(float(tokens[1]), float(tokens[2])))

        # if division
        if tokens[0] == "/" or tokens[0] == "divide":
            print(divide(float(tokens[1]), float(tokens[2])))

        # if square
        if tokens[0] == "square":
            print(square(float(tokens[1])))

        # if cube
        if tokens[0] == "cube":
            print(cube(float(tokens[1])))

        # if power
        if tokens[0] == "pow":
            print(power(float(tokens[1]), float(tokens[2])))

        # if mod
        if tokens[0] == "mod":
            print(mod(float(tokens[1]), float(tokens[2])))
