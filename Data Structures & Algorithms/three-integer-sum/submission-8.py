class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results=[]
        nums.sort()

        for i,num in enumerate(nums):

            # check if num is greater than 0
            if num>0:
                break
            # check if num is the same as last
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            # look for triplets
            l,r=i+1,len(nums)-1
            while l<r:
                tsum=num+nums[l]+nums[r]
                if tsum>0:
                    r-=1
                elif tsum<0:
                    l+=1
                else:
                    results.append([num, nums[l],nums[r]])
                    l+=1
                    r-=1
                    # continue to slide if the next num is the same as prior
                    while l<r and l>0 and nums[l]==nums[l-1]:
                        l+=1
                
        return results