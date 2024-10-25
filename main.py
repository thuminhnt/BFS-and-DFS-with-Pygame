import pygame
import random
import time
from collections import deque
from create_maze import create_maze
from draw_maze import draw_maze
from dfs import dfs
from bfs import bfs

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

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((COLS * CELL_SIZE, ROWS * CELL_SIZE))
pygame.display.set_caption("Maze with Start and End Points")

# Tạo mê cung
maze = create_maze(ROWS, COLS)

# Chạy DFS và hiển thị kết quả trong 10 giây
path_dfs = dfs(screen, maze)
for i in range(10, -1, -1):
    screen.fill(COLOR_WALL)
    draw_maze(screen, maze, visited_dfs=set(path_dfs), path=None)
    font = pygame.font.Font(None, 74)
    text = font.render(str(i), True, (255, 255, 255))
    screen.blit(text, (COLS * CELL_SIZE // 2, ROWS * CELL_SIZE // 2))
    pygame.display.flip()
    time.sleep(1)

# Chạy BFS và hiển thị kết quả trong 10 giây
path_bfs = bfs(screen, maze)
for i in range(10, -1, -1):
    screen.fill(COLOR_WALL)
    draw_maze(screen, maze, visited_bfs=set(path_bfs), path=None)
    font = pygame.font.Font(None, 74)
    text = font.render(str(i), True, (255, 255, 255))
    screen.blit(text, (COLS * CELL_SIZE // 2, ROWS * CELL_SIZE // 2))
    pygame.display.flip()
    time.sleep(1)

# Kết thúc Pygame
pygame.quit()
