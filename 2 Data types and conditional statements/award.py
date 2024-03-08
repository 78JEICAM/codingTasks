# This is a program that determines whether a contestant receives an award in the triathlon competition.
# Requesting to introduce the time taken by contestant for swimming in minutes

swimming = int(input("Please introduce the time taken by contestant for swimming in minutes : "))
print("Time taken for Swimming : ",swimming)

# Requesting to introduce the time taken by contestant for cycling in minutes

cycling = int(input("Please introduce time taken by contestant for cycling in minutes : "))
print("Time taken for Cycling : ",cycling)

# Requesting to introduce the time taken by contestant for running in minutes

running = int(input("Enter time taken by contender for running in minutes : "))
print("Time taken for Running : ",running)

# Calculating and displaying the total time for triathlon

Total_time = swimming+cycling+running
print("Total time taken for triathlon: ",Total_time)

# Condition 1: if : Within qualifying time 0-100 min - (I CORRECTED THIS SECTION BY INCLUDING 100 MIN USIN <= SYMBOL) "Provincial colours". Calculate and display

if (Total_time <= 100):
    print("Provincial Colors")

# Condition 2: else if: Within 5 min of qualifying time - "Half provincial colours". Calculate and display

elif (Total_time > 100 and Total_time <=105):
    print("Provincial Half Colors")

# Condition 3: else if: Within 10 min of qualifying time - "Provincial scroll". Calculate and display

elif (Total_time >105 and Total_time <=110):
    print("Provincial Scroll")

# Condition 4: else : More than 10 min off from the qualifying time - "no award". Calculate and display
else:
    print("No award")