class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results=[]

        for i, c in enumerate(nums):

            if c > 0:
                break
            if i>0 and c == nums[i-1]:
                continue
                #this is to avoid dups
            
            # run two pointer on the idx above
            l=i+1
            r=len(nums)-1
            while l<r:
                three_sum=nums[l]+nums[r]
                if three_sum<-c:
                    l+=1
                elif three_sum>-c:
                    r-=1
                else:
                    results.append([nums[l], nums[r], c])
                    l+=1
                    # since we have found a triplet, we can move l to avoid dups
                    while l < r and l>0 and nums[l]==nums[l-1]:
                        l+=1

        return results