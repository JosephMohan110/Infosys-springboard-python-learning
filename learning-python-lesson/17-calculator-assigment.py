  # calculator


# taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation: add, sub, mul, div")
operation = input("Enter your choice: ")

if operation == "add":
    print("Result =", a + b)

elif operation == "sub":
    print("Result =", a - b)

elif operation == "mul":
    print("Result =", a * b)

elif operation == "div":
    if b != 0:   # to avoid division by zero
        print("Result =", a / b)
    else:
        print("Error! Cannot divide by zero.")

else:
    print("Invalid choice!")
