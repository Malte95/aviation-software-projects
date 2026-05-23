import customtkinter as ctk


# Set up the appearance and theme
ctk.set_appearance_mode("System")  # Adapts to macOS Light or Dark Mode automatically
ctk.set_default_color_theme("blue") # Color theme for UI elements (blue, green, dark-blue)

# Initialize the main application window
app = ctk.CTk()
app.title("Aviation Unit Converter") # Title of the window
app.geometry("600x400")              # Window size: Width x Height in pixels

# Callback function triggered by the dropdown
def update_placeholder(selected_option):
    entry.delete(0, "end")

    if selected_option == "Knots to km/h":
        entry.configure(placeholder_text = "Enter knots")
    elif selected_option == "Feet to meters":
        entry.configure(placeholder_text = "Enter feet")
    elif selected_option == "Gallons to liters":
        entry.configure(placeholder_text = "Enter gallons")
    app.focus_set()

# Add headline
title_label = ctk.CTkLabel(
    master= app,
    text= "Aviation Unit Converter",
    font=("Arial", 32, "bold"),
    text_color= "white"
)
title_label.pack(pady=(30, 5), padx=5)

# Add description
subtitle_label = ctk.CTkLabel(
    master= app,
    text= "Convert common aviation-related units quickly and accurately",
    font=("Arial", 15),
    text_color= "gray70"
)
subtitle_label.pack(pady=(0, 25), padx=25)

# Add a dropdown menu for unit selection
unit_dropdown = ctk.CTkOptionMenu(app, values=["Knots to km/h", "Feet to meters", "Gallons to liters"], width=260, command= update_placeholder)
unit_dropdown.pack(pady=10)

# Add the entry widget with a placeholder
entry = ctk.CTkEntry(app, placeholder_text= "Enter knots", width=260)
entry.pack(pady=20)

# Function to retriev the input
def get_input():
    raw_input = entry.get()

    if not raw_input:
        result_label.configure(text="Please enter a value", text_color = "orange")
        return
    if "," in raw_input:
        result_label.configure(text ="Please use a dot instead of a comma, e.g. 12.5", text_color = "orange")
        return
    try:
        user_input = float(raw_input)
    except ValueError:
        result_label.configure(text = "Please enter a numeric value", text_color = "orange")
        return 
    if user_input < 0:
        result_label.configure(text = "Please enter a positive value", text_color = "orange")
        return
    selected = unit_dropdown.get()
    result = convert_input(user_input, selected)
    result_label.configure(text = result, text_color = "white")
    print("Entered:", user_input)
    print("Selected", selected)

# Function to convert the input
def convert_input(user_input, selected):
    if selected == "Knots to km/h":
        result = f"{user_input * 1.852:.2f} km/h"
        return result
    elif selected == "Feet to meters":
        result = f"{user_input * 0.3048:.2f} m"
        return result
    elif selected == "Gallons to liters":
        result = f"{user_input * 3.78541:.2f} L"
        return result

# Add a single action button
convert_button = ctk.CTkButton(app, text="Convert", width=260, command=get_input)
convert_button.pack(pady=15)

# Add label
result_label = ctk.CTkLabel(
    master= app,
    text= "Result",
    font=("Arial", 24, "bold"),
    text_color= "white"
)
result_label.pack(pady=(25, 10), padx=20)

# Add footer
footer_label = ctk.CTkLabel(
    master= app,
    text= "Built with Python and CustomTkinter",
    font=("Arial", 12),
    text_color= "gray60"
)
footer_label.pack(pady=(10, 0))

# Start the application event loop
app.mainloop()

