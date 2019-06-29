import heapq

def calculate_distances(valGraph, valStarting_vertex):
    distances = {vertex:float('infinity') for vertex in valGraph}
    distances[valStarting_vertex] = 0

    entry_lookup = {}
    pq = []

    for vertex, distance in distances.items():
        entry = [distance, vertex]
        entry_lookup[vertex] = entry
        heapq.heappush(pq, entry)

    while(len(pq) > 0):
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, neighbor_distance in enumerate(valGraph[current_vertex]):
            distance = distances[current_vertex] + neighbor_distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                entry_lookup[neighbor][0] = distance

    print(entry_lookup)

    return distances



valGraph = {"a": {"b", 10}, "b": {"c", 15}}

print(calculate_distances(valGraph, "a"))