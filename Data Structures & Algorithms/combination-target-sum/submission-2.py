class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(index: int, curr:list[int], total:int):
            if total==target:
                res.append(curr.copy())
                return
            if total>target or index==len(nums):
                return
            
            # choose
            curr.append(nums[index])
            dfs(index,curr,total+nums[index])
            curr.pop()
            # choose wo
            dfs(index+1,curr,total)

        dfs(0,[],0)
        return res