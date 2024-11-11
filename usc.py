import heapq

def uniform_cost_search(graph, start, goal):
    # Khởi tạo hàng đợi ưu tiên với chi phí ban đầu là 0 cho đỉnh bắt đầu
    queue = [(0, start)]  # (chi phí, đỉnh)
    # Khởi tạo dictionary để lưu chi phí ngắn nhất đến mỗi đỉnh
    visited = {start: 0}
    # Khởi tạo dictionary để lưu đường đi
    path = {start: None}

    while queue:
        # Lấy đỉnh có chi phí nhỏ nhất trong hàng đợi
        cost, node = heapq.heappop(queue)

        # Nếu đạt đến đỉnh đích, tái tạo và trả về đường đi và chi phí
        if node == goal:
            route = []
            while node is not None:
                route.append(node)
                node = path[node]
            return route[::-1], cost  # Trả về đường đi và chi phí

        # Mở rộng các đỉnh kề của đỉnh hiện tại
        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            # Nếu chưa thăm hoặc tìm thấy đường đi rẻ hơn, cập nhật hàng đợi
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
                path[neighbor] = node

    return None, float("inf")  # Trả về None nếu không có đường đi tới đích

# Ví dụ đồ thị với các đỉnh và trọng số
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 1},
    'C': {'D': 5, 'E': 10},
    'D': {'E': 3},
    'E': {}
}

# Tìm đường đi từ A đến E
route, cost = uniform_cost_search(graph, 'A', 'E')
print("Đường đi ngắn nhất từ A đến E:", route)
print("Chi phí ngắn nhất:", cost)