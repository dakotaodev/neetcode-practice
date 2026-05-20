class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack:list[tuple[int, int]]=[]
        res=0
        for i,h in enumerate(heights):
            starting=i
            while stack and stack[-1][1]>h:
                s_i,s_h=stack.pop()
                area=(i-s_i)*s_h
                res=max(res,area)
                starting=s_i
            stack.append((starting,h))
        
        for i,h in stack:
            res=max(res, (len(heights)-i)*h)
        return res