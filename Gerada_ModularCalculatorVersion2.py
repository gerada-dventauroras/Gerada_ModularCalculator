import math
import time

# Define functions for the calculator
def add(x, y): 
    return x + y

def sub(x, y): 
    return x - y

def mul(x, y): 
    return x * y

def div(x, y): 
    return x / y if y != 0 else "Error: can't divide by 0! :("

# Map out functions for the calculator
calc = {1: add, 2: sub, 3: mul, 4: div}

# Failsafe so the program doesn't crash when a ValueError happens
def input_values(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a number..")

# Ask user for values of the numbers they want to calculate
num1 = input_values("Input the first value: ")
num2 = input_values("Input the second value: ")

# Ask for operation the user wants to perform
choice = ""
while choice not in ["1", "2", "3", "4"]:
    choice = input("Select an operation: 1. Add 2. Subtract 3. Multiply 4. Divide \nEnter choice (1-4): ")

choice = int(choice)

# Display results of said calculation
print("Result:", calc[choice](num1, num2))

time.sleep(4)
exit()
