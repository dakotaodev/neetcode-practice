class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[]
        res=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                s_i,s_h=stack.pop()
                area=(i-s_i)*s_h
                res=max(area,res)
                start=s_i
            stack.append((start,h))
        n=len(heights)
        for i,h in stack:
            area=(n-i)*h
            res=max(area,res)
        return res