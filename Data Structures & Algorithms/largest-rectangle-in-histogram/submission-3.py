class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]

        for index, height in enumerate(heights):
            starting_point=index # track where the current heights is rectangle eligible
            while stack and stack[-1][1]>height:
                # this stack entry is no longer eligible to grow, as the height is larger
                s_starting_point,s_height=stack.pop()
                max_area=max(max_area,s_height*(index-s_starting_point))
                starting_point=s_starting_point
            stack.append((starting_point,height))
        
        # get the leftovers at 
        n=len(heights)
        for i,h in stack:
            max_area=max(max_area, h*(n-i))
        return max_area