class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window=deque()
        l,r=0,0
        res=[]
        while r<len(nums):

            while window and nums[r]>nums[window[-1]]:
                window.pop()
            
            window.append(r)
            
            # check if window[0] is less than l
            if window[0]<l:
                window.popleft()
            
            if r+1>=k:
                res.append(nums[window[0]])
                l+=1
            r+=1
        return res