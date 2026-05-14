import customtkinter as ctk

# 1. Set up the appearance and theme
ctk.set_appearance_mode("System")  # Adapts to macOS Light or Dark Mode automatically
ctk.set_default_color_theme("blue") # Color theme for UI elements (blue, green, dark-blue)

# 2. Initialize the main application window
app = ctk.CTk()
app.title("Aviation Unit Converter") # Title of the window
app.geometry("400x300")              # Window size: Width x Height in pixels

# 3. Start the application event loop
app.mainloop()

