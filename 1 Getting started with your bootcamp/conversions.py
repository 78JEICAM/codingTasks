# Presentation of variables
# num1's value cast to int to remove the decimal point
# num 2's value cast to float to add a decimal point followed by zero
# num3's value cast to a string data so it is no long an int
# string1 cast it to int so it functions like a number
# display all variables as result of casting in seperate lines

#Presentation of variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# num1's value cast to int to remove the decimal point
num1 = 99.23
num1 = int(num1)

# num 2's value cast to float to add a decimal point followed by zero
num2 = 23
num2 = float(num2)

# num3's value cast to a string data so it is no long an int
num3 = 150
num3 = str(num3)

# string1 cast it to int so it functions like a number
string1 = "100"
string1 = int(string1)

# Display all variables in seperate lines as a result of casting
print(num1)
print(num2)
print(num3)
print(string1)
