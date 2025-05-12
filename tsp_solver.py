import random
import math

def solve_tsp_greedy(dist_matrix, start_index=0):
    n = len(dist_matrix)
    visited = [False] * n
    order = [start_index]
    visited[start_index] = True

    current = start_index
    for _ in range(n - 1):
        next_city = min((i for i in range(n) if not visited[i]), key=lambda i: dist_matrix[current][i])
        order.append(next_city)
        visited[next_city] = True
        current = next_city
    return order

def solve_tsp_2opt(dist_matrix, start_index=0):
    route = solve_tsp_greedy(dist_matrix, start_index)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i+1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if route_distance(new_route, dist_matrix) < route_distance(route, dist_matrix):
                    route = new_route
                    improved = True
    return route

def route_distance(order, dist_matrix):
    return sum(dist_matrix[order[i]][order[i+1]] for i in range(len(order)-1))

def solve_tsp_simulated_annealing(dist_matrix, start_index=0, T=10000, cooling_rate=0.995, stopping_T=1e-8):
    n = len(dist_matrix)
    current_order = solve_tsp_greedy(dist_matrix, start_index)
    best_order = list(current_order)
    current_distance = route_distance(current_order, dist_matrix)
    best_distance = current_distance

    while T > stopping_T:
        i, j = sorted(random.sample(range(1, n), 2))
        new_order = current_order[:i] + current_order[i:j][::-1] + current_order[j:]
        new_distance = route_distance(new_order, dist_matrix)

        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / T):
            current_order = new_order
            current_distance = new_distance
            if new_distance < best_distance:
                best_order = new_order
                best_distance = new_distance

        T *= cooling_rate

    return best_order
