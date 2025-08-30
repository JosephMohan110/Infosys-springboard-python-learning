    # factorial assigment

num = int(input("Enter a number to find factorial: "))

# Initialize factorial and counter
factorial = 1
i = 1

# Loop to calculate factorial
while i <= num:
    factorial *= i
    i += 1  # increment counter

print(f"The factorial of {num} is {factorial}")
