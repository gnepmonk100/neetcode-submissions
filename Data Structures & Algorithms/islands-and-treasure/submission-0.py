class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()


        def addRoom(i,j):
            if i < 0 or i >= rows or j<0 or j>=cols or (i,j) in visit or grid[i][j] == -1:
                return
            visit.add((i,j))
            q.append([i,j])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))

        dist = 0
        while q:
            for idx in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
              
