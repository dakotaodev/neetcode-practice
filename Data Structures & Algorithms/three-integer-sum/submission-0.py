class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, a in enumerate(nums):

            # check if a > 0
            if a > 0:
                break

            # check if we are running for a duplicate a
            if i > 0 and a == nums[i-1]:
                continue
            
            # Two Pointer
            L,R=i+1,len(nums)-1
            while L<R:
                threesum = a + nums[L] + nums[R]
                if threesum<0:
                    L+=1
                elif threesum>0:
                    R-=1
                else:
                    results.append([a, nums[L], nums[R]])
                    L+=1
                    while nums[L] == nums[L-1] and L<R:
                        L+=1
            
        return results