import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class BipartiteGraphAnalyzer:
    def __init__(self, edges):
        self.edges = edges
        self.graph = nx.Graph()
        self.graph.add_edges_from(edges)
        self.left = []
        self.right = []
        self.is_bipartite = False
        
    def check_bipartite(self):
        try:
            # Проверяем двудольность и получаем раскраску
            color = nx.bipartite.color(self.graph)
            self.is_bipartite = True
            
            # Разделяем вершины на две доли
            self.left = [node for node in color if color[node] == 0]
            self.right = [node for node in color if color[node] == 1]
            
            return True, None
        except nx.NetworkXError:
            return False, "Граф не является двудольным"

class FordFulkerson:
    def __init__(self, graph, left, right):
        self.graph = graph
        self.left = left
        self.right = right
        self.flow_network = nx.DiGraph()
        self.source = 's'
        self.sink = 't'
        
    def build_flow_network(self):
        # Добавляем вершины источника и стока
        self.flow_network.add_node(self.source)
        self.flow_network.add_node(self.sink)
        
        # Добавляем ребра из источника в левую долю
        for node in self.left:
            self.flow_network.add_edge(self.source, node, capacity=1)
        
        # Добавляем ребра из правой доли в сток
        for node in self.right:
            self.flow_network.add_edge(node, self.sink, capacity=1)
        
        # Добавляем исходные ребра графа (направленные слева направо)
        for u, v in self.graph.edges():
            if u in self.left and v in self.right:
                self.flow_network.add_edge(u, v, capacity=1)
            elif v in self.left and u in self.right:
                self.flow_network.add_edge(v, u, capacity=1)
    
    def find_max_matching(self):
        self.build_flow_network()
        
        # Вычисляем максимальный поток
        flow_value, flow_dict = nx.maximum_flow(self.flow_network, self.source, self.sink)
        
        # Извлекаем паросочетание из потока
        matching = []
        for u in flow_dict:
            if u == self.source or u == self.sink:
                continue
            for v in flow_dict[u]:
                if v != self.source and v != self.sink and flow_dict[u][v] == 1:
                    matching.append((u, v))
        
        return matching

class KuhnAlgorithm:
    def __init__(self, graph, left, right):
        self.graph = graph
        self.left = left
        self.right = right
        self.match_to = {node: None for node in right}
    
    def bpm(self, u, visited):
        for v in self.graph.neighbors(u):
            if v in self.right and v not in visited:
                visited.add(v)
                if self.match_to[v] is None or self.bpm(self.match_to[v], visited):
                    self.match_to[v] = u
                    return True
        return False
    
    def find_max_matching(self):
        for u in self.left:
            self.bpm(u, set())
        
        # Формируем список пар
        matching = [(self.match_to[v], v) for v in self.right if self.match_to[v] is not None]
        return matching

class GraphVisualizer:
    @staticmethod
    def visualize(graph, left, right, matching, title):
        plt.figure(figsize=(12, 8))
        pos = {}
        
        # Располагаем вершины в две колонки
        left_x = 0
        right_x = 2
        left_y = sorted(left, reverse=True)
        right_y = sorted(right, reverse=True)
        
        for i, node in enumerate(left_y):
            pos[node] = (left_x, i)
        
        for i, node in enumerate(right_y):
            pos[node] = (right_x, i)
        
        # Рисуем вершины разными цветами для долей
        nx.draw_networkx_nodes(graph, pos, nodelist=left, node_color='lightblue', node_size=700)
        nx.draw_networkx_nodes(graph, pos, nodelist=right, node_color='lightgreen', node_size=700)
        
        # Рисуем все ребра серым
        nx.draw_networkx_edges(graph, pos, edge_color='gray', width=1, alpha=0.5)
        
        # Рисуем ребра паросочетания красным
        nx.draw_networkx_edges(graph, pos, edgelist=matching, edge_color='red', width=3)
        
        # Подписываем вершины
        nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
        
        plt.title(title, fontsize=14, pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

# Основная программа
if __name__ == "__main__":
    # Исходные данные
    edges = [
        (7, 13), (2, 11), (2, 5), (14, 15), (12, 14), (6, 13),
        (3, 15), (7, 16), (4, 9), (3, 7), (6, 8), (3, 6), (9, 14),
        (10, 11), (4, 12), (5, 14), (2, 7), (5, 10), (2, 6), (9, 10),
        (2, 12), (2, 9), (12, 13), (12, 16), (3, 11), (4, 5),
        (4, 11), (7, 14), (5, 13), (8, 12), (6, 16), (7, 10),
        (9, 13), (6, 14), (3, 5)
    ]
    
    # 1. Проверка двудольности
    analyzer = BipartiteGraphAnalyzer(edges)
    is_bipartite, message = analyzer.check_bipartite()
    
    if not is_bipartite:
        print(message)
        exit()
    
    print("Граф является двудольным")
    print(f"Левая доля: {analyzer.left}")
    print(f"Правая доля: {analyzer.right}")
    
    # 2. Поиск паросочетания алгоритмом Форда-Фалкерсона
    print("\n--- Алгоритм Форда-Фалкерсона ---")
    ff = FordFulkerson(analyzer.graph, analyzer.left, analyzer.right)
    ff_matching = ff.find_max_matching()
    print(f"Максимальное паросочетание: {ff_matching}")
    print(f"Размер паросочетания: {len(ff_matching)}")
    
    # 3. Поиск паросочетания алгоритмом Куна
    print("\n--- Алгоритм Куна ---")
    kuhn = KuhnAlgorithm(analyzer.graph, analyzer.left, analyzer.right)
    kuhn_matching = kuhn.find_max_matching()
    print(f"Максимальное паросочетание: {kuhn_matching}")
    print(f"Размер паросочетания: {len(kuhn_matching)}")
    
    # 4. Визуализация
    print("\nВизуализация результатов...")
    GraphVisualizer.visualize(analyzer.graph, analyzer.left, analyzer.right, [], 
                            "Исходный двудольный граф")
    GraphVisualizer.visualize(analyzer.graph, analyzer.left, analyzer.right, ff_matching, 
                            f"Максимальное паросочетание (Форд-Фалкерсон)\nРазмер: {len(ff_matching)}")
    GraphVisualizer.visualize(analyzer.graph, analyzer.left, analyzer.right, kuhn_matching, 
                            f"Максимальное паросочетание (Алгоритм Куна)\nРазмер: {len(kuhn_matching)}")