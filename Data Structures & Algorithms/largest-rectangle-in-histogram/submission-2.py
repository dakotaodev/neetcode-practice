class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]

        for index, height in enumerate(heights):
            starting_point=index # move back on each pop to track width
            while stack and stack[-1][1]>height:
                s_starting_point,s_height=stack.pop()
                # this means the top of the stack has a height greater than the current height
                # meaning that we need to evaluate its area, as it is no longer eligible to grow at this height
                max_area=max(max_area, s_height*(index-s_starting_point))
                starting_point=s_starting_point
            stack.append((starting_point,height))
        
        # calculate for any leftovers
        n=len(heights)
        for i,h in stack:
            max_area=max(max_area, h*(n-i))
        return max_area
