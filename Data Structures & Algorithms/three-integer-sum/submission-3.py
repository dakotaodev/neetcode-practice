class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort()

        for index, c in enumerate(nums):

            if c>0:
                break
            if index>0 and nums[index-1]==c:
                continue
            
            # two pointer
            l,r=index+1,len(nums)-1
            while l<r:
                threesum=nums[l]+nums[r]
                if threesum<-c:
                    l+=1
                elif threesum>-c:
                    r-=1
                else:
                    results.append([nums[l], nums[r], c])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
            
        return results