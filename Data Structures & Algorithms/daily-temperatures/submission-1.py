class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[] # [index, temp]
        results=[0]*len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                sIdx, sTemp = stack.pop()
                results[sIdx]=idx-sIdx
            stack.append([idx, temp])
        
        return results