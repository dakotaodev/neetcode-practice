class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get counts
        counts={}
        for num in nums:
            c=counts.get(num,0)
            counts[num]=c+1
        # store counts by frequencies
        freqs=[[] for i in range(len(nums)+1)]
        for num,count in counts.items():
            freq=freqs[count]
            freq.append(num)
            freqs[count]=freq

        # traverse top frequencies until we have k nums
        results=[]
        for freq in freqs[::-1]:
            for num in freq:
                results.append(num)
                if len(results)==k:
                    return results