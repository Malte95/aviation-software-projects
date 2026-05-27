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

print(f"Weight: {weight} | Distance: {distance} | Wind strength: {wind_strength} | Wind direction: {wind_direction}")
