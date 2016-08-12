class shopcenter:
    def __init__(self, fish):
        self.fish = set(fish)
        self.neighbors = dict()


Nshops, Nroads, Nfish = map(int, input().strip().split())

for i in range(Nfish):
    shop[i] = shopcenter(map(int, input().strip().split())[1:])

for i in range(Nroads):
    source, destination, time = map(int, input().strip().split())
    shop[source].neighbors[destination] = time


# unvisited = []
# heapq.push(unvisited, (0,0))
# visited = set()

# finishedFishSets = set()
# if new fishset + any(previousFishSet) == completion: return distance

# while unvisited:
#    currentdistance, currentnode, fishpicked = heapq.pop(unvisited)
#    for neighbor, time in shop[currentnode].neighbors.items():
#        #if neighbor not in visited:
#        heapq.push(unvisited, (time + currentdistance, neighbor, fishpicked + shop[neighbor].fish))
#    visited.add(currentnode)


def InQueue(node, mask, cost):
    current = shortest_path[node][mask], (node, mask)
    if current in queue:
        queue.remove(current)
    shortest_path[node][mask] = cost
    current = cost, (node, mask)
    queue.insert(current)


def Dijkstra(src):
    InQueue(src, shops[src], 0)
    while queue:
        cost, (src, current_shops) = heapq.pop(queue)
        for neighbor, time in shop[src].neighbors.items():
            InQueue(neighbor, current_shops | shops[src].fish, cost + time)


def fillShortestPaths():
    for i in range(Nshops):
        for j in range(Nfish):
            shortest_path[i][j] = float('inf')


Dijkstra(0)

best_time = float('inf')
for i in range(Nfish):
    for j in range(i, Nfish):
        if (i | j) == Nfish - 1:
            best_time = min(best_time, max(shortest_path[Nshops][i], shortest_path[Nshops][j]))

print(best_times)
