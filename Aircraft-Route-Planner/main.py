import tkinter as tk
from tkinter import ttk


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


window = tk.Tk()

window.geometry("600x400")
window.title("Aircraft Route Planner")
window.configure(padx=20, pady=20)

title_label = tk.Label(window, text= "Aircraft Route Planner", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

start_label = tk.Label(window, text= "Start Location:")
start_label.pack()

start_dropdown = ttk.Combobox(window, values=list(graph.locations.keys()), state="readonly")
start_dropdown.pack(pady=5)

destination_label = tk.Label(window, text= "Destination:")
destination_label.pack(pady=5)

destination_dropdown = ttk.Combobox(window, values=list(graph.locations.keys()), state="readonly")
destination_dropdown.pack()

start_dropdown.current(0)
destination_dropdown.current(1)

tk.Label(window, text="Location Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack(pady=2)

tk.Label(window, text="Country:").pack()
country_entry = tk.Entry(window)
country_entry.pack(pady=2)

tk.Label(window, text="Site Type:").pack()
type_entry = tk.Entry(window)
type_entry.pack(pady=2)

tk.Label(window, text="Connect to:").pack()
connect_dropdown = ttk.Combobox(window, values=list(graph.locations.keys()), state="readonly")
connect_dropdown.pack(pady=2)

tk.Label(window, text="Distance in km:").pack()
distance_entry = tk.Entry(window)
distance_entry.pack(pady=2)

def add_new_location():
    name = name_entry.get()
    country = country_entry.get()
    site_type = type_entry.get()
    connect_to = connect_dropdown.get()
    distance = distance_entry.get()

    if not name or not country or not site_type or not connect_to or not distance:
        result_label.config(text="Please fill in all fields.")
        return

    new_location = Location(name, country, site_type)
    result = graph.add_location(new_location)

    connection_result = graph.add_connection(name,connect_to,int(distance))

    name_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)

    distance_entry.delete(0, tk.END)

    location_values = list(graph.locations.keys())
    start_dropdown["values"] = location_values
    destination_dropdown["values"] = location_values
    connect_dropdown["values"] = location_values

    result_label.config(text=f"{result}\n{connection_result}")

def find_route():
    start = start_dropdown.get()
    destination = destination_dropdown.get()

    result = graph.shortest_route(start, destination)

    result_label.config(text=result)

add_location_button = tk.Button(window,text="Add Location",command=add_new_location)
add_location_button.pack(pady=10)

find_route_button = tk.Button(window, text="Find Shortest Route", command=find_route)
find_route_button.pack(pady=15)

result_label = tk.Label(window, text="", justify="left", font=("Arial", 11))
result_label.pack(pady=10)

window.mainloop()






        

