class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1

        max_v=0

        while l<r:
            v=min(heights[l], heights[r]) * (r-l)
            max_v=max(max_v, v)

            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return max_v