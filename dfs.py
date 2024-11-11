# DFS sử dụng đệ quy
def dfs(graph, node, visited):
    # Đánh dấu đỉnh hiện tại là đã duyệt
    visited.add(node)
    print(node, end=' ')
    
    # Duyệt các đỉnh liền kề chưa được duyệt của đỉnh hiện tại
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Khởi tạo đồ thị dưới dạng dictionary (từ điển)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': [],
    'E': [],
    'F': []
}

# Tập hợp các đỉnh đã duyệt
visited = set()

# Gọi hàm DFS bắt đầu từ đỉnh 'A'
print("DFS từ đỉnh A:")
dfs(graph, 'A', visited)