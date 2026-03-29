class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort()

        for target_i, target in enumerate(nums):

            if target>0:
                break
            
            if target_i>0 and target==nums[target_i-1]:
                continue # the last value is the same, skip
            
            # run BS on elements above 
            l=target_i+1
            r=len(nums)-1
            while l<r:
                three_sum=target+nums[l]+nums[r]
                if three_sum<0:
                    l+=1
                elif three_sum>0:
                    r-=1
                else:
                    results.append([target, nums[l], nums[r]])
                    l+=1
                    while l<r and l>0 and nums[l]==nums[l-1]:
                        l+=1

        return results