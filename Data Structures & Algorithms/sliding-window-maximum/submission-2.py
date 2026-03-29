class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:  
        
        q=deque()
        results=[]
        l=0
        r=0
        while r<len(nums):

            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if q[0]<l:
                q.popleft()
            
            if (r+1)>=k:
                results.append(nums[q[0]])
                l+=1
            r+=1
        return results