class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars=[[p,s] for p,s in zip(position, speed)]
        cars.sort(reverse=True)

        for p,s in cars:
            t=(target-p)/s
            stack.append(t)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)