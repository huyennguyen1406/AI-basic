def bfs(graph, start, goal):
    # Khởi tạo hàng đợi và danh sách để theo dõi các nút đã duyệt
    queue = deque([start])
    visited = set([start])
    parent = {start: None}  # Để lưu đường đi
    
    while queue:
        node = queue.popleft()
        
        if node == goal:
            # Truy ngược lại để tìm đường đi
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Đường đi từ bắt đầu đến đích
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node  # Lưu lại nút cha để truy ngược

    return None  # Không tìm thấy đường đi

# Đồ thị được biểu diễn dưới dạng từ điển
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'

path = bfs(graph, start, goal)
if path:
    print("Đường đi:", path)
else:
    print("Không tìm thấy đường đi.")
