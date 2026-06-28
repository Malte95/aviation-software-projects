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

bremen = Location(
    "Bremen",
    "Germany",
    "Wing Equipment Center"
)

stade = Location(
    "Stade",
    "Germany",
    "Composite Structures"
)

broughton = Location(
    "Broughton",
    "United Kingdom",
    "Wing Manufacturing"
)

getafe = Location(
    "Getafe",
    "Spain",
    "Aircraft Structures"
)

filton = Location(
    "Filton",
    "United Kingdom",
    "Engineering and Design"
)

test_site = Location(
    "Test Site",
    "Germany",
    "Test Location"
)



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

    def shortest_route(self, start, destination):
        if start in self.locations and destination in self.locations:
            distances = {}
            visited = []
            previous_locations = {}

            for location in self.locations.keys():
                distances[location] = float("inf")

            distances[start] = 0
        
            while len(visited) < len(self.locations):

                smallest_distance = float("inf")
                current_location = None

                for location in self.locations:
                    if location not in visited and distances[location] < smallest_distance:
                        smallest_distance = distances[location]
                        current_location = location
                if current_location is None:
                    break
           
                visited.append(current_location)
                
                for neighbor, distance in self.adjacency_list[current_location].items():
                    new_distance = distances[current_location] + distance

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance 
                        previous_locations[neighbor] = current_location
            
            if distances[destination] == float("inf"):
                return "Route does not exist."


            route = [destination]
            current = destination

            while current != start:
                current = previous_locations[current]
                route.append(current)
                
            route.reverse()

            route_text = " -> ".join(route)

            return (
                "Shortest Route\n\n"
                f"{route_text}\n\n"
                f"Total Distance: {distances[destination]} km"
            )
        
        else:
            return "One or both locations do not exist."

print(hamburg.show_details())

graph = Graph()

graph.add_location(hamburg)
graph.add_location(toulouse)
graph.add_location(mobile)
graph.add_location(bremen)
graph.add_location(stade)
graph.add_location(broughton)
graph.add_location(getafe)
graph.add_location(filton)
graph.add_location(test_site)

graph.add_connection("Filton", "Broughton", 250)
graph.add_connection("Broughton", "Hamburg-Finkenwerder", 950)
graph.add_connection("Broughton", "Toulouse", 1250)
graph.add_connection("Bremen", "Hamburg-Finkenwerder", 120)
graph.add_connection("Stade", "Hamburg-Finkenwerder", 40)
graph.add_connection("Getafe", "Toulouse", 700)
graph.add_connection("Hamburg-Finkenwerder", "Toulouse", 1272)
graph.add_connection("Toulouse", "Mobile", 6160)

print(graph.show_neighbors("Hamburg-Finkenwerder"))
print(graph.show_neighbors("Broughton"))
print(graph.shortest_route("Filton", "Mobile"))

print(
    graph.shortest_route(
        "Hamburg-Finkenwerder",
        "Mobile"
    )
)

print(
    graph.shortest_route(
        "Hamburg-Finkenwerder",
        "Test Site"
    )
)







        

