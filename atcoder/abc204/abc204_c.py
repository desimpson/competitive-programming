import sys

sys.setrecursionlimit(10 ** 6)


class Graph:
    def __init__(self):
        self.graph = dict()

    def add(self, u, v=None):
        if u not in self.graph.keys():
            self.graph[u] = set()
        if v is None:
            self.graph[u] = set() if v is None else self.graph[u].add(v)
        else:
            self.graph[u].add(v)

    def dfs(self, v):
        visited = set()
        self.dfs_helper(v, visited)
        return visited

    def dfs_helper(self, v, visited):
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_helper(neighbour, visited)


def main():
    N, M = map(int, input().split())
    g = Graph()
    [g.add(u) for u in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        g.add(u - 1, v - 1)

    visited_count = sum([len(g.dfs(v)) for v in range(N)])
    print(visited_count)


if __name__ == '__main__':
    main()
