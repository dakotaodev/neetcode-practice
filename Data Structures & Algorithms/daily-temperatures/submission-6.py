class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[] # (day,temp)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1]<t:
                s_i,s_t=stack.pop()
                result[s_i]=i-s_i

            stack.append((i,t))

        return result      