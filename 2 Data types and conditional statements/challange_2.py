# Request user's favourite restaurant using input and store this string as a variable strin_fav

string_fav = input("What is the name of your favourite restaurant? : ")

# Request user's favourite number using input and store it as a variable int_fav and cast it to integer

int_fav = int(input("What is your favourite number ? :" ))

# Printing both statements below and program check - it works

print("Your favourite restaurant is : " , string_fav)
print("Print your favourite number is : " , int_fav)

# Casting variable string_fav to an integer

integer_string_fav = int(string_fav)

# This is causing an error becouse variable is casted to an integer which is not numerical
# Unles as a name of restaurant you will type any digit

# Casting variable to int() doesn't work for text, unless you introduce a digit
# This will cause an error if value is not numerical
# After making researchTo check if data(variable is a digit we can use function isdigit()
# To check if variable is a digit before casting to int() use function isdigit()