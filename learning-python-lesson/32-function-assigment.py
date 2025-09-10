    #    FUNCTION ASSIGMENT


# QUESTION

#WRITE FUNCTION WITH SHOW_NUMERS 
# THAT TAKES N AND PRINT ALL THE NUMERS FROM 0 TO N 
# WITH LABEL TO IDENTIFY THE EVEN AND ODD NUMBER

# def show_numbers(n):
#     print("Number\tType")
#     print("------\t------")
#     for i in range(n + 1):
#         if i % 2 == 0:
#             print(f"{i}\tEVEN")
#         else:
#             print(f"{i}\tODD")

# # Test the function
# show_numbers(10)




#*******************

# QUESTION
#WRITE A PROGRAM THAT CHECKS IF n IS B/W 200 AND 500 PRINT YES 
# IF N IS B/W 200 AND 500. 
# OTHERWISE PRINT NO


# def check_number(N):
#     if 200<= N <=500:
#         print("yes")
#     else:
#         print("NO")
# num=int(input("write a num: "))
# check_number(num)




#************************************


#     QUESTION

#write a function with the name get weather_report 
# that takes the tempture as an argument. 
# if the tempture is less than 22 , it should return "cold". 
# if the tempture is greater than or equal to 22 and less than 35 it should return "warm". 
# if the tempture is greater than or equal to 35 it should return "hot.. 

def get_weather_report(temperature):
    if temperature < 22:
        return "cold"
    elif temperature >= 22 and temperature < 35:
        return "warm"
    else:
        return "hot"

# Test the function with different temperatures
test_temps = [15, 22, 30, 35, 40, 10, 25, 38]

print("Temperature\tWeather Report")
print("-----------\t--------------")
for temp in test_temps:
    report = get_weather_report(temp)
    print(f"{temp}°C\t\t{report}")