class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i,h in enumerate(heights):
            starting=i 
            while stack and stack[-1][1]>h:
                s_i,s_h=stack.pop()
                area=(i-s_i)*s_h
                max_area=max(max_area, area)
                starting=s_i
            stack.append((starting, h))

        n=len(heights)
        for i,h in stack:
            max_area=max(max_area, h*(n-i))
        return max_area