import heapq

def a_star_search(graph, heuristics, start, goal): # Khởi tạo hàng đợi ưu tiên với chi phí ban đầu là 0 cho đỉnh bắt đầu
    queue = [(0, start)]  # (f(n), đỉnh)
    g_cost = {start: 0} # Khởi tạo dictionary để lưu chi phí ngắn nhất từ điểm bắt đầu đến mỗi đỉnh
    path = {start: None} # Khởi tạo dictionary để lưu đường đi
    while queue: # Lấy đỉnh có chi phí f(n) nhỏ nhất trong hàng đợi
        _, node = heapq.heappop(queue)
        # Nếu đạt đến đỉnh đích, tái tạo và trả về đường đi và chi phí
        if node == goal:
            route = []
            while node is not None:
                route.append(node)
                node = path[node]
            return route[::-1], g_cost[goal]  # Trả về đường đi và chi phí

        # Mở rộng các đỉnh kề của đỉnh hiện tại
        for neighbor, edge_cost in graph[node].items():
            new_g_cost = g_cost[node] + edge_cost
            # Tính toán chi phí f(n) = g(n) + h(n)
            f_cost = new_g_cost + heuristics[neighbor]
            # Nếu chưa thăm hoặc tìm thấy đường đi rẻ hơn, cập nhật hàng đợi
            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                heapq.heappush(queue, (f_cost, neighbor))
                path[neighbor] = node
    return None, float("inf")  # Trả về None nếu không có đường đi tới đích
# Ví dụ đồ thị với các đỉnh và cạnh
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 1},
    'C': {'D': 5, 'E': 10},
    'D': {'E': 3},
    'E': {}
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
route, cost = a_star_search(graph, heuristics, 'A', 'E')
print("Đường đi ngắn nhất từ A đến E theo A* Search:", route)
print("Chi phí ngắn nhất:", cost)