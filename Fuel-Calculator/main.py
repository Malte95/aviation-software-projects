weight = float(input("Enter weight:"))
distance = float(input("Enter distance:"))
wind_strength = float(input("Enter wind strength:"))
wind_direction = input("Headwind or tailwind: ")


if wind_direction.lower() == "headwind":
    print("Consumption increases")
elif wind_direction.lower() == "tailwind":
    print("Consumption decreases")
else:
    print("Invalid input")

def calculate_fuel(weight, distance, wind_strength, wind_direction):
    base_consumption_per_km = 5
    consumption = base_consumption_per_km * distance
    return consumption

fuel_consumption = calculate_fuel(weight, distance, wind_strength, wind_direction)


print(f"Weight: {weight} | Distance: {distance} | Wind strength: {wind_strength} | Wind direction: {wind_direction} | Fuel consumption: {fuel_consumption}")
