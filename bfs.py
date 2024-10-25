from collections import deque
from draw_maze import draw_maze

# Kích thước của ma trận
ROWS = 100
COLS = 100

def bfs(screen, maze):
    queue = deque([(1, 1)])  # Bắt đầu từ vị trí (1, 1)
    visited = set()
    parent = {}  # Để lưu trữ đường đi

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        draw_maze(screen, maze, visited_bfs=visited)

        if maze[x][y] == 'E':
            path = []
            while (x, y) != (1, 1):
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append((1, 1))
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= ROWS or ny >= COLS:
                continue  # Vượt quá giới hạn ma trận

            if maze[nx][ny] == '#' or (nx, ny) in visited:
                continue  # Gặp tường hoặc đã thăm

            queue.append((nx, ny))
            parent[(nx, ny)] = (x, y)
