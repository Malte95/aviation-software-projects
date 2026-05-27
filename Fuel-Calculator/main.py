weight = float(input("Enter weight:"))
distance = float(input("Enter distance:"))
wind_strength = float(input("Enter wind strength:"))
wind_direction = input("Headwind or tailwind: ")

def calculate_fuel(weight, distance, wind_strength, wind_direction):
    base_consumption_per_km = 5
    weight_factor = 0.0001
    scaled_weight = weight / 100
    consumption = base_consumption_per_km * distance * ( 1 + scaled_weight * weight_factor)
    return consumption

if wind_direction.lower() not in ["headwind", "tailwind"]:
    print("Invalid input")
else:
    fuel_consumption = calculate_fuel(weight, distance, wind_strength, wind_direction)
    print(f"Weight: {weight} | Distance: {distance} | Wind strength: {wind_strength} | Wind direction: {wind_direction} | Fuel consumption: {fuel_consumption:.2f} L")
