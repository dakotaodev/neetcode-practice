class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get counts
        counts={}
        for n in nums:
            counts[n]=counts.get(n,0)+1
        # map to frequencies
        freqs=[[] for i in range(len(nums)+1)]
        for num,count in counts.items():
            f=freqs[count]
            f.append(num)
            freqs[count]=f
        # return the top k results
        results=[]
        for i in range(len(nums),-1,-1):
            f=freqs[i]
            for n in f:
                results.append(n)
                if len(results)==k:
                    return results        