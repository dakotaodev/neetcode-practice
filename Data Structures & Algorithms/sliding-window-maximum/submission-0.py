class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results=[]
        l=r=0
        q=deque()

        while r < len(nums):
            
            # first check if we can pop from the top of the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove from the lhs if not in the window
            if l > q[0]:
                q.popleft()
            
            # if we have a valid window, store the max
            if r + 1 >= k:
                results.append(nums[q[0]])
                l+=1
            r+=1
        return results