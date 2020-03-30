class Solution:

    def maxAreaOfIsland(self, grid) -> int:

        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        area = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    area = max(self._detect(i, j), area)

        return area

    def _detect(self, i, j):
        if self._test_invalid_point(i, j) or self.grid[i][j] != 1:
            return 0

        self.grid[i][j] = -1

        return 1 + self._detect(i + 1, j) + self._detect(i, j + 1) + self._detect(i - 1, j) + self._detect(i, j - 1)

    def _test_invalid_point(self, i, j):
        return i < 0 or i >= self.m or j >= self.n or j < 0