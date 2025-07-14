def read_grid(filename):
    with open(filename, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]
    return grid

def find_start(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'S':
                return r, c
    return None

def neighbors(grid, r, c):
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != '#':
                yield nr, nc

def dfs(grid, start, end_char='E'):
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        (r, c), path = stack.pop()
        if grid[r][c] == end_char:
            return path
        for nr, nc in neighbors(grid, r, c):
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))
    return None

def write_path(grid, path, out_filename):
    with open(out_filename, 'w') as f:
        for r, c in path:
            f.write(grid[r][c])


def main(input_file='input.txt', output_file='output.txt'):
    grid = read_grid(input_file)
    start = find_start(grid)
    if not start:
        print("No start point 'S' found.")
        return

    path = dfs(grid, start)
    if path is None:
        print("No path found from S to E.")
        return

    write_path(grid, path, output_file)
    print(f"Path written to {output_file}")

if __name__ == '__main__':
    main(input(), input())
