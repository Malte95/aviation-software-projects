aircrafts = {
    1: {
        "name": "A320",
        "base_consumption": 4.5,
        "range_km": 6300,
        "typical_passengers": 150,
        "max_takeoff_weight": 79000,
        "cruise_speed": 840
    },
    2: {
        "name": "A330",
        "base_consumption": 22.0,
        "range_km": 8200,
        "typical_passengers": 345,
        "max_takeoff_weight": 242000,
        "cruise_speed": 880
    },
    3: {
        "name": "A350",
        "base_consumption": 6.0,
        "range_km": 16000,
        "typical_passengers": 370,
        "max_takeoff_weight": 280000,
        "cruise_speed": 900
    }
}
routes = {
    1: {
        "origin": "Hamburg-Finkenwerder",
        "destination": "Toulouse",
        "distance": 1350
    },
    2: {
        "origin": "Toulouse",
        "destination": "Getafe",
        "distance": 650
    },
    3: {
        "origin": "Broughton",
        "destination": "Toulouse",
        "distance": 1100
    }
}


def calculate_fuel(weight, distance, wind_strength, wind_direction, selected_aircraft):
    base_consumption_per_km = selected_aircraft["base_consumption"]
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

def calculate_range_utilization(distance, selected_aircraft):
    return (distance / selected_aircraft["range_km"]) * 100

def calculate_flight_time(distance, selected_aircraft):
    return distance / selected_aircraft["cruise_speed"]

def get_range_status(range_utilization):
    if range_utilization < 50:
        return "Normal"
    elif range_utilization < 90:
        return "High utilization"
    else:
        return "Near maximum range"
try:

    print("Select aircraft:")
    print("1 - A320")
    print("2 - A330")
    print("3 - A350")
    
    print("Select route:")
    print("1 - Hamburg-Finkenwerder to Toulouse")
    print("2 - Toulouse to Getafe")
    print("3 - Broughton to Toulouse")
    aircraft_choice = int(input("Select aircraft: "))
    route_choice = int(input("Select route: "))
    if aircraft_choice not in aircrafts:
        print("Please select a valid aircraft")
    elif route_choice not in routes:
        print("Please select a valid route")
    else:
        selected_aircraft = aircrafts[aircraft_choice]
        weight = float(input("Enter weight:"))
        wind_strength = float(input("Enter wind strength:"))
        wind_direction = input("Headwind or tailwind: ").lower()
        fuel_price_per_liter = float(input("Enter fuel price per liter (€):"))
        selected_route = routes[route_choice]
        distance = selected_route["distance"]
        range_utilization = calculate_range_utilization(distance, selected_aircraft)
        flight_time = calculate_flight_time(distance, selected_aircraft)
        status = get_range_status(range_utilization)

        if weight < 0 or wind_strength < 0 or fuel_price_per_liter < 0:
            print("Please enter a positive number")

        else: 
            if weight > selected_aircraft["max_takeoff_weight"]:
                print("Warning: Weight exceeds maximum takeoff weight")
        
        
            if distance > selected_aircraft["range_km"]:
                print("Warning: Distance exceeds aircraft range")

            if wind_direction not in ["headwind", "tailwind"]:
                print("Invalid input")
            else:
                fuel_consumption = calculate_fuel(weight, distance, wind_strength, wind_direction, selected_aircraft)
                fuel_cost = fuel_consumption * fuel_price_per_liter
                print("\n===== FUEL CALCULATION =====")
                print(f"Aircraft: {selected_aircraft['name']}")
                print(f"Range: {selected_aircraft['range_km']} km")
                print(f"Passengers: {selected_aircraft['typical_passengers']}")
                print(f"Cruise Speed: {selected_aircraft['cruise_speed']} km/h")
                print(f"Weight: {weight} kg")
                print(f"Route: {selected_route['origin']} to {selected_route['destination']}")
                print(f"Route Distance: {distance} km")
                print(f"Flight Time: {flight_time:.2f} h")
                print(f"Range Utilization: {range_utilization:.2f} %")
                print(f"Status: {status}")
                print(f"Wind: {wind_direction} {wind_strength} km/h")
                print(f"Fuel Consumption: {fuel_consumption:.2f} L")
                print(f"Fuel Cost: €{fuel_cost:.2f}")
except ValueError:
    print("Please enter numeric values only")


