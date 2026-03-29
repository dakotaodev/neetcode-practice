class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       results=[]
       self.backtrack(0,results,[],nums)
       return results

    def backtrack(self,i,results,curr,nums):
        
        if i==len(nums):
            results.append(curr.copy())
            return
        
        # decide with 
        curr.append(nums[i])
        self.backtrack(i+1,results,curr,nums)
        curr.pop()

        # decide wo
        self.backtrack(i+1,results,curr,nums)