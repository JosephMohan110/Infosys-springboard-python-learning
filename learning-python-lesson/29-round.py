     #  ROUND


# The round() function returns a floating-point number rounded to the specified number of decimals.
# Rounded floating-point numbeR
# The most important rule to understand is how ROUND handles the digit 5. The universal rule is:
# If the digit you are looking at is 5 or greater, you round up the previous digit.
# If the digit you are looking at is 4 or less, you leave the previous digit as it is (round down).
# Example: Rounding 3.14159 to two decimal places.
# The second decimal is 4.
# The next digit (the third decimal) is 1, which is less than 5.
# Therefore, we leave the 4 alone. Result: 3.14
# Example: Rounding 2.726 to two decimal places.
# The second decimal is 2.
# The next digit (the third decimal) is 6, which is 5 or greater.
# Therefore, we round the 2 up to 3. Result: 2.73





print(round(7.9999))

print(round(4.44))
print(type(round(4)))  # after digit no.of gigit indagill class will float

print(round(4,2))
print(type(round(4,2))) # its class will int not float because given number(4) is int. given number want to be float and no.of.digit is aso want, then only class beacame float

print(round(4.4,2))
print(type(round(4.4,2)))  # itsa class will float because given number is in float and there is no.of.digit      

print(round(5.5))
print(round(3.641,2))
print(round(6.3333,0))