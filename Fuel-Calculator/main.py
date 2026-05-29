def calculate_fuel(weight, distance, wind_strength, wind_direction):
    base_consumption_per_km = 5
    weight_factor = 0.0001
    scaled_weight = weight / 100
    wind_factor = 0.001
    wind_effect = wind_strength * wind_factor
    consumption = base_consumption_per_km * distance * ( 1 + scaled_weight * weight_factor)
    if wind_direction.lower() == "headwind":
        consumption *= 1 + wind_effect
    elif wind_direction.lower() == "tailwind":
         consumption *= 1 - wind_effect
    return consumption
try:
    aircrafts = {
    1: {
        "name": "A320",
        "base_consumption": 4.5
    },
    2: {
        "name": "A330",
        "base_consumption": 22.0
    },
    3: {
        "name": "A350",
        "base_consumption": 6.0
    }
}
    print("Select aircraft:")
    print("1 - A320")
    print("2 - A330")
    print("3 - A350")
    aircraft_choice = int(input("Select aircraft: "))
    if aircraft_choice not in aircrafts:
        print("Please select a valid aircraft")
    else:
        selected_aircraft = aircrafts[aircraft_choice]
        print(selected_aircraft["name"])
        print(selected_aircraft["base_consumption"])
        weight = float(input("Enter weight:"))
        distance = float(input("Enter distance:"))
        wind_strength = float(input("Enter wind strength:"))
        wind_direction = input("Headwind or tailwind: ")

        if weight < 0 or distance < 0 or wind_strength < 0:
            print("Please enter a positive number")
        else:
            if wind_direction.lower() not in ["headwind", "tailwind"]:
                print("Invalid input")
            else:
                fuel_consumption = calculate_fuel(weight, distance, wind_strength, wind_direction)
                print(f"Selected aircraft: {selected_aircraft} | Weight: {weight} | Distance: {distance} | Wind strength: {wind_strength} | Wind direction: {wind_direction} | Fuel consumption: {fuel_consumption:.2f} L")
except ValueError:
    print("Please enter numeric values only")


