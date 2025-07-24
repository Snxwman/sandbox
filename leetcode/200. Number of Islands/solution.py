from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited: set[tuple[int, int]] = set()

        def get_neighbors(row: int, col: int) -> list[tuple[int, int]]:
            neighbors: list[tuple[int, int]] = []
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for drow, dcol in directions:
                new_row, new_col = row + drow, col + dcol
                if new_row in range(rows) and new_col in range(cols):
                    neighbors.append((new_row, new_col))

            return neighbors

        def find_island_bounds(row: int, col: int):
            q: deque[tuple[int, int]] = deque()

            visited.add((row, col))
            q.append((row, col))

            while len(q) > 0:
                node = q.pop()
                for neighbor in get_neighbors(*node):
                    row, col = neighbor
                    if neighbor not in visited and grid[row][col] == '1':
                        q.append(neighbor)
                        visited.add(neighbor)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    islands += 1
                    find_island_bounds(row, col)

        return islands
