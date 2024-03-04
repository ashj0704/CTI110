# Jordan Ash

# 3/3/24

# P2LAB1

# Performing mathematical calculations and displays.

def calculate_gas_cost(miles_per_gallon, cost_per_gallon, distance):
    gallons_needed = distance / miles_per_gallon
    total_cost = gallons_needed * cost_per_gallon
    return total_cost

miles_per_gallon = float(input("Enter the car's gas mileage (miles per gallon): "))
cost_per_gallon = float(input("Enter the cost of gas (dollars per gallon): "))

distance_20_miles = 20
distance_75_miles = 75
distance_500_miles = 500

print(f"Gas cost for 20 miles: ${calculate_gas_cost(miles_per_gallon, cost_per_gallon, distance_20_miles):.2f}")
print(f"Gas cost for 75 miles: ${calculate_gas_cost(miles_per_gallon, cost_per_gallon, distance_75_miles):.2f}")
print(f"Gas cost for 500 miles: ${calculate_gas_cost(miles_per_gallon, cost_per_gallon, distance_500_miles):.2f}")
