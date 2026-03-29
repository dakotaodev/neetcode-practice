class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results=[0]*len(nums)

        # prefix product
        prefix=1
        for i,n in enumerate(nums):
            results[i]=prefix
            prefix*=n
        
        # postfix product
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            n=nums[i]
            results[i]*=postfix
            postfix*=n
        
        return results
