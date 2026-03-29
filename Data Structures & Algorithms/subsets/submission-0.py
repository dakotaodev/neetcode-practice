class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[]
        currset=[]
        self.helper(0,nums,subsets,currset)
        return subsets
    
    def helper(self,i,nums,subsets,currset):

        if i>=len(nums):
            subsets.append(currset.copy())
            return
        
        # decide to include i
        currset.append(nums[i])
        self.helper(i+1,nums,subsets,currset)
        currset.pop()

        # decide to not include i
        self.helper(i+1,nums,subsets,currset)