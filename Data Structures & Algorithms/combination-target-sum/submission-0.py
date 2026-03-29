class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()

        def backtrack(i,curr,total):
            if target==total:
                res.append(curr.copy())
                return
            
            for j in range(i,len(nums)):
                if nums[j]+total>target:
                    return
                
                curr.append(nums[j])
                backtrack(j,curr,total+nums[j])
                curr.pop()
            

        backtrack(i=0,curr=[],total=0)
        return res


