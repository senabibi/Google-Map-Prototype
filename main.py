import heapq
from complex import my_graph
from menu import display_menu, get_user_choice, get_city_name, get_k_value, get_destination_city, display_invalid_choice

class Graph:
    def __init__(self):
        self.graph = {}
        self.current_city = None

    def enter_city(self, city):
        self.current_city = city
        self.add_vertex(city)

    def print_current_city(self):
        if self.current_city:
            print(f"Current City: {self.current_city}")
        else:
            print("Current City not set.")

    def list_k_closest_cities(self, k):
        if self.current_city:
            distances = {city: float('inf') for city in self.graph}
            distances[self.current_city] = 0
            heap = [(0, self.current_city)]

            while heap:
                current_distance, current_city = heapq.heappop(heap)

                if current_distance > distances[current_city]:
                    continue

                for neighbor, weight in self.graph[current_city].items():
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))

            closest_cities = sorted(distances, key=distances.get)[1:k+1]  # Exclude the current city
            print(f"{k} closest cities to {self.current_city}: {', '.join(closest_cities)}")
        else:
            print("Current City not set.")

    def find_shortest_path_to(self, destination_city):
        if self.current_city:
            distances = {city: float('inf') for city in self.graph}
            distances[self.current_city] = 0
            previous = {city: None for city in self.graph}
            heap = [(0, self.current_city)]

            while heap:
                current_distance, current_city = heapq.heappop(heap)

                if current_distance > distances[current_city]:
                    continue

                for neighbor, weight in self.graph[current_city].items():
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current_city
                        heapq.heappush(heap, (distance, neighbor))

            path = self._get_shortest_path(previous, destination_city)
            print(f"Shortest path from {self.current_city} to {destination_city}: {', '.join(path)}")
        else:
            print("Current City not set.")

    def _get_shortest_path(self, previous, destination_city):
        path = []
        while destination_city:
            path.insert(0, destination_city)
            destination_city = previous[destination_city]
        return path

    def add_vertex(self, city):
        if city not in self.graph:
            self.graph[city] = {}

    def remove_vertex(self, city):
        if city in self.graph:
            del self.graph[city]
            for neighbor in self.graph:
                if city in self.graph[neighbor]:
                    del self.graph[neighbor][city]

    def add_edge(self, city1, city2, weight):
        self.add_vertex(city1)
        self.add_vertex(city2)
        self.graph[city1][city2] = weight
        self.graph[city2][city1] = weight

    def remove_edge(self, city1, city2):
        if city1 in self.graph and city2 in self.graph[city1]:
            del self.graph[city1][city2]
            del self.graph[city2][city1]

    def __str__(self):
        return str(self.graph)


graph_data = my_graph


graph = Graph()

# Add vertices and edges to the graph
for city, neighbors in graph_data.items():
    for neighbor, weight in neighbors.items():
        graph.add_edge(city, neighbor, weight)

# Menu-driven interface
while True:
    display_menu()

    choice = get_user_choice()

    if choice == 'a':
        city = get_city_name()
        graph.enter_city(city)
    elif choice == 'b':
        graph.print_current_city()
    elif choice == 'c':
        k = get_k_value()
        graph.list_k_closest_cities(k)
    elif choice == 'd':
        destination_city = get_destination_city()
        graph.find_shortest_path_to(destination_city)
    elif choice == 'x':
        break
    else:
        display_invalid_choice()
