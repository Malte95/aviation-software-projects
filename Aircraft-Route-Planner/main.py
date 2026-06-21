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

    def add_connection(self, start, destination, distance):
        if start in self.locations and destination in self.locations:
            if destination in self.adjacency_list[start]:
                return "Connection already exists."
            else:
                self.adjacency_list[start][destination] = distance
                self.adjacency_list[destination][start] = distance
                return "Connection added successfully."
        else:
            return "One or both locations do not exist."

    def show_all_locations(self):
        return "Available Locations\n\n" + "\n".join(self.locations.keys())

        

