import heapq

def greedy_search(graph, heuristics, start, goal):
    # Khởi tạo hàng đợi ưu tiên với chi phí heuristic cho đỉnh bắt đầu
    queue = [(heuristics[start], start)]  # (ước lượng chi phí, đỉnh)
    # Tạo một tập hợp các đỉnh đã thăm để tránh thăm lại
    visited = set()
    # Khởi tạo dictionary để lưu đường đi
    path = {start: None}
    while queue:
        # Lấy đỉnh có ước lượng chi phí nhỏ nhất trong hàng đợi
        _, node = heapq.heappop(queue)

        # Nếu đạt đến đỉnh đích, tái tạo và trả về đường đi
        if node == goal:
            route = []
            while node is not None:
                route.append(node)
                node = path[node]
            return route[::-1]  # Trả về đường đi

        # Đánh dấu đỉnh hiện tại là đã thăm
        visited.add(node)
        # Mở rộng các đỉnh kề của đỉnh hiện tại
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics[neighbor], neighbor))
                path[neighbor] = node
    return None  # Trả về None nếu không tìm thấy đường đi tới đích
# Ví dụ đồ thị với các đỉnh và cạnh
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E'],
    'E': []
}
# Heuristic (ước lượng khoảng cách đến đích) cho từng đỉnh
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}
# Tìm đường đi từ A đến E
route = greedy_search(graph, heuristics, 'A', 'E')
print("Đường đi từ A đến E theo Greedy Search:", route)