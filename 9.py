from collections import deque

class BipartiteGraph:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = set()
        for u, v in edges:
            self.nodes.update({u, v})
        self.adj = {}
        for node in self.nodes:
            self.adj[node] = []
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        # Разделение на доли (предполагаем, что граф двудольный)
        self.left = set()
        self.right = set()
        self._bipartition()

    def _bipartition(self):
        """Разделение вершин на две доли (BFS-раскраска)"""
        if not self.nodes:
            return
        
        color = {}
        start_node = next(iter(self.nodes))
        queue = deque([start_node])
        color[start_node] = 0
        self.left.add(start_node)
        
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    if color[v] == 0:
                        self.left.add(v)
                    else:
                        self.right.add(v)
                    queue.append(v)

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.flow = {}
        
    def bfs(self, s, t, parent):
        visited = set()
        queue = deque()
        queue.append(s)
        visited.add(s)
        
        while queue:
            u = queue.popleft()
            for v in self.graph.adj[u]:
                if v not in visited and (u, v) not in self.flow or self.flow[(u, v)] > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == t:
                        return True
        return False
    
    def max_matching(self):
        # Добавляем источник и сток
        s = 'source'
        t = 'sink'
        self.graph.adj[s] = list(self.graph.left)
        self.graph.adj[t] = []
        for node in self.graph.right:
            self.graph.adj[node].append(t)
        
        # Инициализация потока
        for u, v in self.graph.edges:
            self.flow[(u, v)] = 0
            self.flow[(v, u)] = 0
        for u in self.graph.left:
            self.flow[(s, u)] = 0
            self.flow[(u, s)] = 0
        for v in self.graph.right:
            self.flow[(v, t)] = 0
            self.flow[(t, v)] = 0
        
        parent = {}
        max_flow = 0
        
        while self.bfs(s, t, parent):
            path_flow = float('Inf')
            v = t
            while v != s:
                u = parent[v]
                if (u, v) in self.flow:
                    path_flow = min(path_flow, self.flow[(u, v)])
                else:
                    path_flow = min(path_flow, 1)  # Все пропускные способности 1
                v = u
            
            v = t
            while v != s:
                u = parent[v]
                if (u, v) in self.flow:
                    self.flow[(u, v)] -= path_flow
                    self.flow[(v, u)] += path_flow
                v = u
            
            max_flow += path_flow
        
        # Восстанавливаем паросочетание
        matching = []
        for u in self.graph.left:
            for v in self.graph.adj[u]:
                if v != t and self.flow[(v, u)] == 1:
                    matching.append((u, v))
                    break
        
        return matching

class KuhnAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.match_to = {v: None for v in self.graph.right}
    
    def bpm(self, u, visited):
        for v in self.graph.adj[u]:
            if v in self.graph.right and v not in visited:
                visited.add(v)
                if self.match_to[v] is None or self.bpm(self.match_to[v], visited):
                    self.match_to[v] = u
                    return True
        return False
    
    def max_matching(self):
        for u in self.graph.left:
            self.bpm(u, set())
        return [(self.match_to[v], v) for v in self.graph.right if self.match_to[v] is not None]

def print_matching(matching):
    print("Максимальное паросочетание (размер = {}):".format(len(matching)))
    for pair in matching:
        print("{} - {}".format(pair[0], pair[1]))

if __name__ == "__main__":
    edges = [
        (7, 13), (2, 11), (2, 5), (14, 15), (12, 14), (6, 13),
        (3, 15), (7, 16), (4, 9), (3, 7), (6, 8), (3, 6), (9, 14),
        (10, 11), (4, 12), (5, 14), (2, 7), (5, 10), (2, 6), (9, 10),
        (2, 12), (2, 9), (12, 13), (12, 16), (3, 11), (4, 5),
        (4, 11), (7, 14), (5, 13), (8, 12), (6, 16), (7, 10),
        (9, 13), (6, 14), (3, 5)
    ]
    
    print("Строим двудольный граф...")
    graph = BipartiteGraph(edges)
    print("Левая доля:", graph.left)
    print("Правая доля:", graph.right)
    
    print("\n--- Алгоритм Форда-Фалкерсона ---")
    ff = FordFulkerson(graph)
    ff_matching = ff.max_matching()
    print_matching(ff_matching)
    
    print("\n--- Алгоритм Куна ---")
    kuhn = KuhnAlgorithm(graph)
    kuhn_matching = kuhn.max_matching()
    print_matching(kuhn_matching)