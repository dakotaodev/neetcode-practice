class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[] # (index, temp)
        results = [0]*len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                s_index, s_temp = stack.pop()
                results[s_index]=index-s_index
            stack.append([index, temp])
        return results