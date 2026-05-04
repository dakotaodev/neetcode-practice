class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars=list(zip(position,speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        for p,s in cars:
            t=(target-p)/s
            stack.append(t)
            while len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
            
        return len(stack)