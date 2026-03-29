class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest=0
        stack=[] # starting_point, height

        for i,h in enumerate(heights):
            starting=i
            while stack and stack[-1][1]>h:
                s_i,s_h=stack.pop()
                largest=max(largest,s_h*(i-s_i))
                starting=s_i
            stack.append((starting,h))

        for i,h in stack:
            largest=max(largest,h*(len(heights)-i))

        return largest