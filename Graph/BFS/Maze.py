class Solution:
    def bfs(self, maze, r, c, dr, dc, visited):
        m, n = len(maze), len(maze[r])
        if r == dr and dc == c:
            return True
        if (r, c) in visited:
            return False
        visited.add((r,c))
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        for ir, ic in directions:
            currr, currc = r, c
            while 0 <= currr + ir < m and 0 <= currc + ic < n  and maze[currr + ir][currc + ic] != 1:
                currr += ir
                currc += ic
            if self.bfs(maze, currr, currc, dr, dc, visited) == True:
                return True
        return False

    def hasPath(self, maze, start, destination):
        if not maze or not maze[0]:
            return False
        return self.bfs(maze, start[0], start[1], destination[0], destination[1], set())

print(Solution().hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
[0,4],
[4,4]))