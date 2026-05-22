import customtkinter as ctk


# 1. Set up the appearance and theme
ctk.set_appearance_mode("System")  # Adapts to macOS Light or Dark Mode automatically
ctk.set_default_color_theme("blue") # Color theme for UI elements (blue, green, dark-blue)

# 2. Initialize the main application window
app = ctk.CTk()
app.title("Aviation Unit Converter") # Title of the window
app.geometry("400x300")              # Window size: Width x Height in pixels

# Add a dropdown menu for unit selection
unit_dropdown = ctk.CTkOptionMenu(app, values=["Knots to km/h", "Feet to meters", "Gallons to liters"])
unit_dropdown.pack(pady=10)

# Add the entry widget with a placeholder
entry = ctk.CTkEntry(app, placeholder_text= "Enter knots")
entry.pack(pady=20)

# Function to retriev the input
def get_input():
    raw_input = entry.get()

    if not raw_input:
        my_label.configure(text="Please enter a value")
        return
    if "," in raw_input:
        my_label.configure(text ="Please use a dot instead of a comma, e.g. 12.5")
        return
    try:
        user_input = float(raw_input)
    except ValueError:
        my_label.configure(text = "Please enter a numeric value")
        return 
    if user_input < 0:
        my_label.configure(text = "Please enter a positive value")
        return
    selected = unit_dropdown.get()
    result = convert_input(user_input, selected)
    my_label.configure(text = result)
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
convert_button = ctk.CTkButton(app, text="Convert", command=get_input)
convert_button.pack(pady=15)

# Add label
my_label = ctk.CTkLabel(
    master= app,
    text= "Result",
    font=("Arial", 20),
    text_color= "white"
)
my_label.pack(pady=40, padx=20)

# 3. Start the application event loop
app.mainloop()

