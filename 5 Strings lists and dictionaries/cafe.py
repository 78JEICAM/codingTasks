# Define the menu list with at least four items sold in the cafe
menu = ["Pierogi", "Bigos", "Żurek", "Kotlet schabowy"]

# Define the stock dictionary with stock value for each item on the menu
stock = {
    "Pierogi": 100,
    "Bigos": 50,
    "Żurek": 30,
    "Kotlet schabowy": 70
}

# Define the price dictionary with prices for each item on the menu in British pounds sterlings
price = {
    "Pierogi": 5.99,
    "Bigos": 6.49,
    "Żurek": 4.99,
    "Kotlet schabowy": 8.99
}

# Initialize a variable to store the total stock worth in the cafe
total_stock_worth = 0

# Loop through the menu list to calculate the total stock worth
for item in menu:
    # Calculate the item value by multiplying the stock value by the price value
    item_value = stock[item] * price[item]
    # Add the item value to the total stock worth
    total_stock_worth += item_value

# Print out the result of the calculation
print("Total stock worth in the cafe:", total_stock_worth)
