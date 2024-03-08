# Task objectives:
# 1 Create a new file called while.py.
# 2 Write a program that always asks the user to enter a number.
# 3 When the user enters -1, the program should stop requesting the user to enter a number,
# 4 The program must then calculate the average of the numbers entered, excluding the -1.
# 5 Make use of the while loop repetition structure to implement the program.

# Friendly greeting to the user

print("Hello user!")

num = 0  # Variable to store the number entered by the user 

sum = 0  # Variable to store sum of numbers

count = 0  # Variable to count input numbers

# This will loop until the value of num is not -1

while num != -1:

    # Request user to input the value of any number 

    num = int(input("Please enter any number or -1 to quit : "))

    # if num is not -1 add num to the sum and increase the count by 1

    if num != -1:

        sum = sum + num

        count = count + 1

# Print sum/count which is the required to calculate average of numbers

print("The average of numbers introduced by user, excluding -1 is : ", sum/count)