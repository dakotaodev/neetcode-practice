class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results=[1] * len(nums)

        # first, at each index calculate the product of all elements to the left
        prefix=1
        for i,n in enumerate(nums):
            results[i]=prefix
            prefix*=n
        
        # now, at each index, calcualte the product of all elements to the right
        postfix=1
        for i in range(len(nums)-1, -1,-1):
            results[i]=postfix*results[i]
            postfix*=nums[i]
        
        return results