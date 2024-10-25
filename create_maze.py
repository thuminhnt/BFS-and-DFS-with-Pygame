import random

def create_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)] # Tạo ma trận toàn tường
    start_row, start_col = 1, 1
    maze[start_row][start_col] = '.' # Đặt điểm bắt đầu
    walls = [(start_row, start_col, start_row + dr, start_col + dc) for dr, dc in [(0, 2), (2, 0), (0, -2), (-2, 0)] if 0 <= start_row + dr < rows and 0 <= start_col + dc < cols]
    random.shuffle(walls) # Trộn ngẫu nhiên các tường

    while walls:
        r1, c1, r2, c2 = walls.pop()
        if maze[r2][c2] == '#':
            maze[r2][c2] = '.'
            maze[(r1 + r2) // 2][(c1 + c2) // 2] = '.'
            for dr, dc in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                nr, nc = r2 + dr, c2 + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '#':
                    walls.append((r2, c2, nr, nc))
            random.shuffle(walls)

    maze[0][1] = 'S' # Đặt điểm bắt đầu
    maze[rows - 1][cols - 2] = 'E' # Đặt điểm kết thúc
    return maze
