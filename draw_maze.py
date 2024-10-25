import pygame

# Kích thước của ma trận
ROWS = 100
COLS = 100

CELL_SIZE = 7.5  # Kích thước mỗi ô trong pixel

# Màu sắc cho các ô
COLOR_WALL = (0, 0, 0)  # Đen cho tường
COLOR_PATH = (255, 255, 255)  # Trắng cho đường đi
COLOR_START = (0, 255, 0)  # Xanh lá cho điểm bắt đầu
COLOR_END = (255, 0, 0)  # Đỏ cho điểm kết thúc
COLOR_VISITED_DFS = (173, 216, 230)  # Xanh nhạt cho ô đã thăm DFS
COLOR_VISITED_BFS = (144, 238, 144)  # Xanh lá nhạt cho ô đã thăm BFS
COLOR_CURRENT = (255, 255, 0)  # Vàng cho ô hiện tại
COLOR_PATH_RESULT = (255, 20, 147)  # Màu hồng cho đường đi kết quả

def draw_maze(screen, maze, visited_dfs=set(), visited_bfs=set(), path=None):
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == '#':
                color = COLOR_WALL
            elif maze[i][j] == 'S':
                color = COLOR_START
            elif maze[i][j] == 'E':
                color = COLOR_END
            elif path and (i, j) in path:
                color = COLOR_PATH_RESULT  # Màu cho đường đi kết quả
            elif (i, j) in visited_dfs:
                color = COLOR_VISITED_DFS
            elif (i, j) in visited_bfs:
                color = COLOR_VISITED_BFS
            else:
                color = COLOR_PATH

            # Vẽ ô
            pygame.draw.rect(screen, color,
                             (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))  # Vẽ ô

    pygame.display.flip() # Cập nhật màn hình
