
class City:
    def __init__(self, roads=None, visited=False):
        self.roads = roads or []
        self.visited = visited


graph = {}
cr = None
cl = None
cost = 0


def solve():
    global graph, cr, cl, cost

    n, m, cl, cr = list(map(int, input().split()))
    graph = dict(((i, City()) for i in range(1, n + 1)))
    cost = 0

    for _ in range(0, m):
        s, d = list(map(int, input().split()))
        graph[s].roads.append(d)
        graph[d].roads.append(s)

    if cr > cl:
        print(cl * n)
        return

    traverse([], 0, True)
    print(cost)


def traverse(roads, road_count, start=True):
    global graph, cr, cl, cost

    if road_count == 0:
        if start:
            for i, city in graph.items():

                if not city.visited:
                    cost += cl      # first library in the sub-graph
                    road_count = len(city.roads)
                    city.visited = True

                    if road_count > 0:
                        traverse(city.roads, road_count, False)
    else:
        for r in roads:
            city = graph[r]

            if not city.visited:
                if cr > cl:
                    cost += cl
                else:
                    cost += cr
                city.visited = True
                road_count += len(city.roads)
                traverse(city.roads, road_count, False)

            road_count -= 1

        if road_count == 0:     # sub-graph finished
            traverse([], 0, True)


def main():
    q = int(input())
    for _ in range(0, q):
        solve()


main()

