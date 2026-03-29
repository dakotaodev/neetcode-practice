class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        results = [0] * len(temperatures)
        stack:list[int, int] = []

        for t, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackI, stackT = stack.pop()
                results[stackI]=t-stackI
            stack.append((t, temp))

        return results