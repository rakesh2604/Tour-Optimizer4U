import argparse
import csv
import json
from collections import namedtuple
from tsp_solver import solve_tsp_greedy, solve_tsp_2opt, solve_tsp_simulated_annealing
import math

# Define Place tuple
Place = namedtuple('Place', ['name', 'lat', 'lon'])

# Haversine function to calculate the distance between two points on the Earth
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Difference in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance

def load_places_from_csv(filename, limit=None):
    places = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for i, row in enumerate(reader):
            if limit and i >= limit:
                break
            name, lat, lon = row
            places.append(Place(name, float(lat), float(lon)))
    return places

def main():
    parser = argparse.ArgumentParser(description='Solve the Traveling Salesman Problem.')
    parser.add_argument('--csv', required=True, help='CSV file with places')
    parser.add_argument('--start', required=True, help='Start location')
    parser.add_argument('--should-return', action='store_true', help='Return to the start location')
    parser.add_argument('--algo', choices=['greedy', '2opt', 'simulated-annealing'], default='greedy', help='Algorithm to use')
    parser.add_argument('--limit', type=int, help='Limit number of places for faster testing')
    args = parser.parse_args()

    # Load places with the optional limit
    places = load_places_from_csv(args.csv, args.limit)
    
    # Ensure the start location exists in the CSV
    start_index = next((i for i, place in enumerate(places) if place.name == args.start), None)
    if start_index is None:
        print(f"Start location '{args.start}' not found in CSV.")
        return
    
    # Compute the distance matrix
    dist_matrix = [[haversine(p1.lat, p1.lon, p2.lat, p2.lon) for p2 in places] for p1 in places]
    
    # Choose algorithm
    if args.algo == 'greedy':
        order = solve_tsp_greedy(dist_matrix, start_index)
    elif args.algo == '2opt':
        order = solve_tsp_2opt(dist_matrix, start_index)
    else:
        order = solve_tsp_simulated_annealing(dist_matrix, start_index)

    # Print the result
    total_distance = sum(dist_matrix[order[i]][order[i+1]] for i in range(len(order)-1))
    if args.should_return:
        order.append(order[0])  # Return to start
        total_distance += dist_matrix[order[-2]][order[0]]
    
    print("Optimal tour:")
    for i, index in enumerate(order):
        print(f"{i+1}) {places[index].name}")
    
    print(f"Total distance: {total_distance:.2f} km")
    
    # Save result as GeoJSON
    geojson = {"type": "FeatureCollection", "features": []}
    coordinates = [(places[i].lon, places[i].lat) for i in order]
    geojson["features"].append({
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": coordinates
        },
        "properties": {"name": "Optimal Tour"}
    })
    
    with open("route.geojson", "w") as f:
        json.dump(geojson, f)
    print("Route written to route.geojson")

if __name__ == "__main__":
    main()
