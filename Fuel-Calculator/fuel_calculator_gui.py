import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Aircraft Fuel Calculator")
app.geometry("800x750")

aircrafts = {
    "A320": {
        "base_consumption": 4.5,
        "range_km": 6300,
        "typical_passengers": 150,
        "max_takeoff_weight": 79000,
        "cruise_speed": 840
    },
    "A330": {
        "base_consumption": 22.0,
        "range_km": 8200,
        "typical_passengers": 345,
        "max_takeoff_weight": 242000,
        "cruise_speed": 880
    },
    "A350": {
        "base_consumption": 6.0,
        "range_km": 16000,
        "typical_passengers": 370,
        "max_takeoff_weight": 280000,
        "cruise_speed": 900
    }
}

routes = {
    "Hamburg-Finkenwerder → Toulouse": {
        "origin": "Hamburg-Finkenwerder",
        "destination": "Toulouse",
        "distance": 1350
    },
    "Toulouse → Getafe": {
        "origin": "Toulouse",
        "destination": "Getafe",
        "distance": 650
    },
    "Broughton → Toulouse": {
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

    consumption = (
        base_consumption_per_km
        * distance
        * (1 + scaled_weight * weight_factor)
    )

    if wind_direction == "headwind":
        consumption *= 1 + wind_effect
    elif wind_direction == "tailwind":
        consumption *= 1 - wind_effect

    return consumption

title_label = ctk.CTkLabel(
    app,
    text="Aircraft Fuel Calculator",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=30)

aircraft_label = ctk.CTkLabel(
    app,
    text="Select Aircraft"
)
aircraft_label.pack(pady=(20, 5))

aircraft_dropdown = ctk.CTkComboBox(
    app,
    values=["A320", "A330", "A350"]
)
aircraft_dropdown.pack()

weight_label = ctk.CTkLabel(
    app,
    text="Weight (kg)"
)
weight_label.pack(pady=(20,5))

weight_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter weight in kg"
)
weight_entry.pack()

route_label = ctk.CTkLabel(
    app,
    text="Select Route"
)
route_label.pack(pady=(20, 5))

route_dropdown = ctk.CTkComboBox(
    app,
    values=[
        "Hamburg-Finkenwerder → Toulouse",
        "Toulouse → Getafe",
        "Broughton → Toulouse"
    ]
)
route_dropdown.pack()

wind_label = ctk.CTkLabel(
    app,
    text="Wind Strength (km/h)"
)
wind_label.pack(pady=(20, 5))

wind_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter wind strength"
)
wind_entry.pack()

fuel_price_label = ctk.CTkLabel(
    app,
    text="Fuel Price per Liter (€)"
)
fuel_price_label.pack(pady=(20, 5))

fuel_price_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter fuel price"
)
fuel_price_entry.pack()

wind_direction_label = ctk.CTkLabel(
    app,
    text="Wind Direction"
)
wind_direction_label.pack(pady=(20, 5))

wind_direction_dropdown = ctk.CTkComboBox(
    app,
    values=["headwind", "tailwind"]
)
wind_direction_dropdown.pack()

def handle_calculation():
    try:
        aircraft = aircraft_dropdown.get()
        route = route_dropdown.get()
        weight = float(weight_entry.get())
        wind_strength = float(wind_entry.get())
        fuel_price = float(fuel_price_entry.get())
        wind_direction = wind_direction_dropdown.get()

        if weight < 0 or wind_strength < 0 or fuel_price < 0:
            result_label.configure(
                text="Please enter positive values only."
            )
            return

        selected_aircraft = aircrafts[aircraft]
        selected_route = routes[route]
        distance = selected_route["distance"]

        fuel_consumption = calculate_fuel(
            weight,
            distance,
            wind_strength,
            wind_direction,
            selected_aircraft
        )

        fuel_cost = fuel_consumption * fuel_price

        result_label.configure(
            text=f"Fuel Consumption: {fuel_consumption:.2f} L\nFuel Cost: €{fuel_cost:.2f}"
        )

    except ValueError:
        result_label.configure(
            text="Please enter valid numeric values."
        )

calculate_button = ctk.CTkButton(
    app,
    text="Calculate",
    command=handle_calculation
)
calculate_button.pack(pady=25)

result_label = ctk.CTkLabel(
    app,
    text="Result will appear here",
    font=("Arial", 16)
)
result_label.pack(pady=10)

app.mainloop()