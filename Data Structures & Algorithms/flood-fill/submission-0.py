class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original_color: int = image[sr][sc]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque([(sr,sc)])
        ROWS, COLS= len(image), len(image[0])
        seen: set[tuple[int, int]] = set()
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                image[r][c]=color

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if (
                        0<=nr<ROWS
                        and 0<=nc<COLS
                        and image[nr][nc]==original_color
                        and (nr,nc) not in seen
                    ):
                        q.append((nr,nc))
                        seen.add((nr,nc))
        return image