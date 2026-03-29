class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # steps
        # 1. create frequency buckets
        # 2. get counts
        # 3. for each count, num, add that to the freq bucket
        # 4. iterate backwards through freq bucket to get the top k

        counts={}
        freq=[ [] for i in range(len(nums)+1)]

        for num in nums:
            counts[num]=counts.get(num,0)+1
        
        for num, count in counts.items():
            f=freq[count]
            f.append(num)
            freq[count]=f
        
        results=[]
        for i in range(len(nums),0,-1):
            f=freq[i]
            for num in f:
                results.append(num)
                if len(results)==k:
                    return results




