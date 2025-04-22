import math

print("="*30)
print("      SIMPLE CALCULATOR      ")
print("="*30)

print("Available operations:")
print(" +   Addition")
print(" -   Subtraction")
print(" *   Multiplication")
print(" /   Division")
print(" %   Modulo")
print(" **  Power")
print(" //  Floor Division")
print(" sqrt  Square Root")
print(" abs   Absolute Value")
print("-" * 30)

operator = input("Enter an operator: ")
single_operand_operator = ["sqrt", "abs"]
print("-" * 30)

if operator in single_operand_operator:
    num = float(input("Enter a number: "))

    if operator == "sqrt":
        if num<0:
            print("Can't calculate square root of a negative number.")

        else:
            result = math.sqrt(num)
            print(f"Square root of {num} is {round(result, 2)}")

    elif operator == "abs":
            result = math.fabs(num)
            print(f"Absolute value of {num} is {round(result, 2)}")

elif operator in ["+", "-", "*", "/", "%", "**", "//"]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {round(result, 2)}")

    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {round(result, 2)}")

    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {round(result, 2)}")

    elif operator == "/":
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {round(result, 2)}")

    elif operator == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {round(result, 2)}")

    elif operator == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {round(result, 2)}")

    elif operator == "//":
        if num2 == 0:
            print("Floor division by zero is not allowed.")
        else:
            result = num1 // num2
            print(f"{num1} // {num2} = {round(result, 2)}")

else:
    print(f"'{operator}' is not a valid operator.")

print("="*30)
print("       Calculation Done       ")
print("="*30)