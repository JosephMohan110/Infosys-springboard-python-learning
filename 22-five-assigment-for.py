# 1. Write program that reads a number N and prints square of N rows and N columns using numbers starting from 1

# 1. Square of N rows and N columns

N = int(input("Enter number: "))
num = 1
for i in range(N):
    for j in range(N):
        print(num, end=" ")
        num += 1
    print()


#***************

# 2. Write a program that reads a number N and prints two Right Angled Triangles of N rows, using numbers starting from 1.

N = int(input("Enter number: "))

# First Triangle
print("First Triangle:")
num = 1
for i in range(1, N+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Second Triangle
print("\nSecond Triangle:")
num = 1
for i in range(N, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


#******************************

# 3. Write a program to print the factorial of N. 
# Factorial is the product of all positive integers less than or equal to N.

N = int(input("Enter number: "))
fact = 1
for i in range(1, N+1):
    fact *= i
print("Factorial of", N, "is:", fact)


#*******************************

# 4. Write a program that reads a string and prints the count of vowels in the string.

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)



#*************************************

# 5. Given two numbers X and N, write a program to print the sum of N terms in the given series.
# Series: (x)^2, (xx)^2, (xxx)^2, ... N terms

X = int(input("Enter value of X: "))
N = int(input("Enter number of terms (N): "))

sum_series = 0
term = ""

for i in range(1, N+1):
    term = str(X) * i  # Repeat X i times
    value = int(term) ** 2
    sum_series += value
    print(f"Term {i}: {term}^2 = {value}")

print("Sum of series:", sum_series)
