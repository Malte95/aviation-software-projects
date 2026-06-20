class Location:
    def __init__(self, name, country, site_type):
        self.name = name
        self.country = country
        self.site_type = site_type
    
    def show_details(self):
        return f"""Location Details
Name: {self.name}
Country: {self.country}
Type: {self.site_type}"""

hamburg = Location(
    "Hamburg-Finkenwerder",
    "Germany",
    "Final Assembly Line"
)

toulouse = Location(
    "Toulouse",
    "France",
    "Final Assembly Line"
)

mobile = Location(
    "Mobile",
    "USA",
    "Final Assembly Line"
)

print(hamburg.show_details())

class Graph:
    def __init__(self):
        self.locations = {}
        self.adjacency_list = {}

    def add_location(self, location):
        if location.name in self.locations:
            return "Location already exists."
        else:
            self.locations[location.name] = location
            self.adjacency_list[location.name] = {}
            return f"{location.name} added successfully."
        

