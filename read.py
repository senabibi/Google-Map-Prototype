def create_city_distances_dict(adjacent_cities_file, city_distances_file):
   
  # İlk olarak komşu şehirleri içeren dosyayı okuyarak bir sözlük oluşturuyoruz.
    adjacent_cities_dict = create_adjacency_list(adjacent_cities_file)

    # Şehir mesafelerini içeren dosyayı okuyarak ilgili bilgileri ekliyoruz.
    with open(city_distances_file, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip().split(';')
    city_index = header.index('City Name')

    graph = {}
    for line in lines[1:]:
        data = line.strip().split(';')
        city_name = data[city_index]
        if city_name in adjacent_cities_dict:
            city_data = {}
            for i in range(2, len(header)):
                neighbor_city = header[i]
                distance = data[i]
                if neighbor_city in adjacent_cities_dict[city_name] and distance and distance != '0':
                    city_data[neighbor_city] = int(distance)

            graph[city_name] = city_data

    return graph

# Önceki adjacency_list oluşturan fonksiyon bu
def create_adjacency_list(file_path):
    graph = {}
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip().split(',')
        key = line[0]
        values = set(line[1:])
        graph[key] = values

    return graph

adjacent_cities_file = 'adjacent_cities.txt'
city_distances_file = 'CityDistances.txt'
graph = create_city_distances_dict(adjacent_cities_file, city_distances_file)
with open('my_graph.py', 'w') as output_file:
    output_file.write(f'graph = {graph}\n')
