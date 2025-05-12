# 🧭 Traveling Salesman City-Tour Optimizer

This project solves a variation of the **Traveling Salesman Problem (TSP)**—a classic algorithmic challenge of finding the shortest possible route that visits a list of cities and returns to the origin. The optimizer implements multiple solving strategies including **Greedy**, **2-opt**, and **Simulated Annealing**, calculates inter-city distances using the **Haversine formula**, and provides both CLI interaction and visualization support.

---

## 🚀 Features

* 📂 **CSV Input** – Load city coordinates from a structured CSV file.
* 🌍 **Haversine Distance** – Accurate great-circle distance calculation between two geographic points.
* 🧠 **TSP Algorithms**:

  * Greedy Algorithm
  * 2-opt Optimization
  * Simulated Annealing
* 🗺️ **GeoJSON Export** – Generates `.geojson` file for easy map-based visualization.
* 💻 **Command-Line Interface (CLI)** – Allows selection of algorithm, start city, and optional limits.
* 📊 **Matplotlib Plotting** – Visualizes the tour path and city nodes.

---

## 📚 Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Usage](#usage)
4. [Command-Line Arguments](#command-line-arguments)
5. [Output](#output)
6. [GeoJSON Export](#geojson-export)
7. [Algorithms Explained](#algorithms-explained)
8. [Use Case Example](#use-case-example)
9. [License](#license)
10. [Contributing](#contributing)

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/rakesh2604/Tour-Optimizer4U.git
cd Tour-Optimizer4U
pip install -r requirements.txt
```

---

## 🏠 Project Structure

```bash
Tour-Optimizer4U/
│
├── tsp.py              # CLI entry point
├── tsp_solver.py       # Core TSP algorithms (Greedy, 2-opt, Simulated Annealing)
├── plot_route.py       # Route plotting with matplotlib
├── Distance.py         # Haversine distance calculation
├── places.csv          # Sample city coordinates
├── route.geojson       # Generated output file
└── requirements.txt    # Python dependencies
```

---

## ▶️ Usage

Make sure `places.csv` is set up with valid city names and coordinates.

Example run:

```bash
python tsp.py --csv places.csv --start "Eiffel Tower" --algo 2opt --limit 50 --should-return
```

---

## 🦾 Command-Line Arguments

| Argument          | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| `--csv`           | Path to input CSV file. Example: `places.csv`                    |
| `--start`         | Name of the starting city. Example: `"Place 1"`                  |
| `--limit`         | (Optional) Max number of cities to include.                      |
| `--algo`          | TSP algorithm: `greedy` (default), `2opt`, `simulated-annealing` |
| `--should-return` | (Optional) Return to start city at end of route                  |

---

## ✅ Output

After execution, you will receive:

* ✔️ A printed city tour in optimal order
* 📏 Total distance in kilometers
* 🗺️ `route.geojson` file for map visualization

**Sample Output:**

```
Optimal tour:
1) Eiffel Tower
2) Place 3
3) Place 2
...
Total distance: 132.45 km
Route written to route.geojson
```

---

## 🌐 GeoJSON Export

The tool generates a `route.geojson` file with the full tour. You can preview it on:

👉 [geojson.io](https://geojson.io/)

1. Open the website
2. Upload your `route.geojson` file
3. View your city-tour route instantly

---

## 🧠 Algorithms Explained

### 🔹 Greedy

Starts from a city and repeatedly visits the nearest unvisited city. Fast, but not always optimal.

### 🔹 2-opt

Improves an initial route by swapping segments to shorten the tour. More accurate, slightly slower.

### 🔹 Simulated Annealing

Explores many possible solutions, accepting worse ones occasionally to avoid local minima. Best suited for larger datasets.

---

## 🔍 Use Case Example

Run a 2-opt optimized tour starting from **"Place 1"**, limited to 50 cities, and returning to start:

```bash
python tsp.py --csv places.csv --start "Place 1" --limit 50 --algo 2opt --should-return
```

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Fork the repo
* Submit feature suggestions or bug reports
* Create pull requests to improve algorithms or UX

---
