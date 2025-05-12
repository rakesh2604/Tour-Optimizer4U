import matplotlib.pyplot as plt

def plot_tour(places, tour):
    lats = [places[i].lat for i in tour]
    lons = [places[i].lon for i in tour]
    names = [places[i].name for i in tour]

    plt.figure(figsize=(8, 6))
    plt.scatter(lons, lats, c='red', marker='o')
    for i, name in enumerate(names):
        plt.text(lons[i] + 0.001, lats[i] + 0.001, name, fontsize=9)
    for i in range(len(tour) - 1):
        plt.arrow(lons[i], lats[i], lons[i+1] - lons[i], lats[i+1] - lats[i],
                  color='blue', head_width=0.005, length_includes_head=True)
    plt.title("Optimized TSP Tour")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("route_plot.png")
    plt.show()
