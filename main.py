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
    if not entry.get():
        my_label.configure(text="Please enter a valid number")
        return
    user_input = float(entry.get())
    selected = unit_dropdown.get()
    result = convert_input(user_input, selected)
    my_label.configure(text = result)
    print("Entered:", user_input)
    print("Selected", selected)

# Function to convert the input
def convert_input(user_input, selected):
    if selected == "Knots to km/h":
        result = str(user_input * 1.852) + " km/h"
        return result
    elif selected == "Feet to meters":
        result = str(user_input * 0.3048) + " m"
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

