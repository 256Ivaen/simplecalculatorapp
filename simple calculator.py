# Defining functions
def sum_of_two_numbers(first, second):
    result = first + second
    return result

def difference_between_two_numbers(first, second):
    result = first - second
    return result

def multiplication_of_two_numbers(first, second):
    result = first * second
    return result

def division_of_two_numbers(first, second):
    if second != 0:
        return first/second

    else:
        return "Error: Number cannot be divided by zero"

#Assigning oparators
operation = input("Choose an operation: + - * /")
a = float(input("First number: "))
b = float(input("Second number: "))

if operation == "+":
    result = sum_of_two_numbers(a, b)

elif operation == "-":
    result = difference_between_two_numbers(a, b)

elif operation == "*":
    result = multiplication_of_two_numbers(a, b)

elif operation == "/":
    result = division_of_two_numbers(a, b)

else:
    print("Error: invalid operation")

print("The result is: ",result)