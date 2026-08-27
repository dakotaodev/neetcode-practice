class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res: int = None
        count=0
        for n in nums:
            if n == res:
                count+=1
            else:
                if count==0:
                    res=n
                    count+=1
                else:
                    count-=1
        return res