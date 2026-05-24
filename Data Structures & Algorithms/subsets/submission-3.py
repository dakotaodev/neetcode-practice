class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]

        def dfs(i):
            if i==len(nums):
                res.append(curr.copy())
                return
            
            # choose not
            dfs(i+1)
            # choose
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
        
        dfs(0)
        return res