class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts={}
        freq=[[] for i in range(len(nums)+1)]

        #get counts
        for num in nums:
            counts[num]=counts.get(num,0) + 1
        
        # add to freqs
        for num, count in counts.items():
            freq[count].append(num)

        # traverse backwards through the freqs to get the k most freq
        results=[]
        for f in freq[::-1]:
            for num in f:
                results.append(num)
                if len(results)==k:
                    return results