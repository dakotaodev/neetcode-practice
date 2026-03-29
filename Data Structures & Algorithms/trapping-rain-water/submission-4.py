class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r=0,len(height)-1
        maxLeft,maxRight=height[l],height[r]
        trapped=0
        while l<r:
            if maxLeft<maxRight:
                l+=1
                maxLeft=max(maxLeft,height[l])
                trapped+=maxLeft-height[l]
            else:
                r-=1
                maxRight=max(maxRight,height[r])
                trapped+=maxRight-height[r]
        return trapped