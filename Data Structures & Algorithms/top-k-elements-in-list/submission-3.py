class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        freqs=[[] for i in range(len(nums)+1)]

        # get counts
        for n in nums:
            count=counts.get(n,0)
            counts[n]=count+1
        
        # add to freqs
        for num,count in counts.items():
            f=freqs[count]
            f.append(num)
            freqs[count]=f
        
        # build result by traversing freqs
        results=[]
        for f in freqs[::-1]:
            for n in f:
                results.append(n)
                if len(results)==k:
                    return results
        