class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a result list of zeros
        # create a stack that contain (day #, temperature)
        # for each temperature 
        # ....while stack, check if the top of the stack is less in temp
        # ........if yes, pop from stack and update result
        # ........if not, add to stack
        # return results
        results = [0 for i in range(0, len(temperatures))]
        stack=[]
        for idx, temp in enumerate(temperatures):

            while stack and stack[-1][1]<temp:
                # update results
                s_i,s_temp=stack.pop()
                results[s_i]=idx-s_i

            stack.append([idx, temp])
        
        return results