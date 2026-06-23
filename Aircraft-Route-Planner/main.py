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

    def show_neighbors(self, location_name):
        if location_name in self.locations:
            neighbor_lines = []

            for neighbor, distance in self.adjacency_list[location_name].items():
                neighbor_lines.append(f"{neighbor} ({distance} km)")

        else:
            return "Location does not exist."
        
        return f"Neighbors of {location_name}\n\n" + "\n".join(neighbor_lines)

    def route_exists(self, start, destination):
        if start in self.locations and destination in self.locations:
            queue = [start]
            visited = [start]

            while queue:
                current_location = queue.pop(0)

                if current_location == destination:
                    return "Route exists."

                for neighbor in self.adjacency_list[current_location].keys():
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
            return "Route does not exist."

        else:
            return "One or both locations do not exist."

graph = Graph()

print(graph.add_location(hamburg))
print(graph.add_location(toulouse))
print(graph.add_location(mobile))

print(
    graph.add_connection(
        "Hamburg-Finkenwerder",
        "Toulouse",
        1272
    )
)

print(
    graph.route_exists(
        "Hamburg-Finkenwerder",
        "Toulouse"
    )
)

print(
    graph.route_exists(
        "Hamburg-Finkenwerder",
        "Mobile"
    )
)

        

