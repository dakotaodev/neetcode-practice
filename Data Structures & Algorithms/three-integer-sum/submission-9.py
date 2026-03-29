class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results=[]

        for i,c in enumerate(nums):

            if c>0:
                break
            if i>0 and c==nums[i-1]:
                continue

            l,r=i+1,len(nums)-1
            while l<r:
                tsum=nums[l]+nums[r]+c
                if tsum>0:
                    r-=1
                elif tsum<0:
                    l+=1
                else:
                    results.append([nums[l], nums[r],c])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
            
        return results
            