class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[] 

        positions=[[p,s] for p,s in zip(position, speed)]
        positions.sort(reverse=True)

        for p,s in positions:
            t=(target-p)/s
            stack.append(t)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)