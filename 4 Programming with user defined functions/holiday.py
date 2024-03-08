# hotel_cost(num_nights): This function calculates the total cost of the hotel stay based on the number of nights.
# plane_cost(city_flight): This function calculates the cost of the flight based on the chosen city. If the city is not in the list, it returns "city not listed" and zero cost.
# car_rental(rental_days): This function calculates the total cost of car rental based on the number of days.
# holiday_cost(num_nights, city_flight, rental_days): This function calculates the total holiday cost by summing up the costs from the other functions.
# The main part of the code prompts the user to input the city they will fly to. If the city is not listed, it exits the program. Otherwise, it proceeds to ask for the number of nights and car rental days, calculates the total cost, and displays the holiday details.

def hotel_cost(num_nights):
    # Assume hotel cost per night is $100
    return num_nights * 100

def plane_cost(city_flight):
    # Define flight costs for different cities
    city_costs = {
        "New York": 300,
        "Los Angeles": 250,
        "London": 400,
        "Paris": 350,
        "Tokyo": 500,
        "Sydney": 450,
        "Warsaw": 200,
        "Krakow": 180   
    }
    # Check if the city is in the list, if not, return "city not listed" and zero cost
    if city_flight in city_costs:
        return city_costs[city_flight]
    else:
        print("City not listed")
        return 0

def car_rental(rental_days):
    # Assume daily car rental cost is $50
    return rental_days * 50

def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

if __name__ == "__main__":
    city_flight = input("Enter the city you will be flying to (New York, Los Angeles, London, Paris, Tokyo, Sydney, Warsaw, Krakow): ")
    
    # Check if the city is in the list, if not, return zero cost
    if plane_cost(city_flight) == 0:
        exit()
    
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    print("\nHoliday Details:")
    print(f"City of Flight: {city_flight}")
    print(f"Number of Nights at Hotel: {num_nights}")
    print(f"Number of Days for Car Rental: {rental_days}")
    print(f"Total Holiday Cost: ${total_cost}")