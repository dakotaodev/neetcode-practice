class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # approach: two pointer
        # return: indicies of the values that match value
        # but this it needs to be incremented by one

        l,r=0,len(numbers)-1
        while l<r:
            curr = numbers[l] + numbers[r]
            if curr<target:
                l+=1
            elif curr>target:
                r-=1
            else:
                return [l+1,r+1]