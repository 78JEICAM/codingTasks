# Write code to output the pattern of asterisk with an if-else statement in combination with a single for loop 
# Calculating the number of stars to print based on a condition. 
# If row_number is less than to the row_count then we are going to print a number of asteriks equal to the row_number. 
# On the other hand once our row_number exceeds our row_count we will start reducing the number of stars to print.
# I will use(2 *) to get a repeated string.

row_count = 5 
#  Starting condition
start = 1 
# Ending condition, I will use(2 *) to get a repeated string
end = (2 * row_count) 
# Creating a variable row_number in a range of start and end condition is met we create another variable star_count
for row_number in range(start, end):
    # Variable star_count counting peak and if else start reducing the number of asterisks
    star_count = row_number if row_number < row_count else end - row_number
    print("*" * star_count) # Print statement with display asterisks as many as in star_count variable (i removed the second loop)
print()