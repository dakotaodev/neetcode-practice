class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, a in enumerate(nums):
            
            # we know that a must be greater than 0 to find a valid triplet
            if a>0:
                break
            
            # skip if prior value is the same to avoid dups
            if i>0 and a==nums[i-1]:
                continue

            # use two points to find a value bc s.t. b + c = -a
            b=i+1
            c=len(nums)-1

            while b<c:
                current=nums[b]+nums[c]
                if current < -a:
                    b+=1
                elif current> -a:
                    c-=1
                else:
                    results.append([a,nums[b], nums[c]])
                    b+=1
                    while nums[b]==nums[b-1] and b<c:
                        b+=1
                    

        return results


