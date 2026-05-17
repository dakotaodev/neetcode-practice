class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res=int("".join([str(d) for d in digits]))+1

        return [int(r) for r in str(res)]