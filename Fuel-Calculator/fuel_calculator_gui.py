import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Aircraft Fuel Calculator")
app.geometry("800x600")

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

app.mainloop()