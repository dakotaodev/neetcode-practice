class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def backtrack(i:int,curr:list,total:int):

            if total==target:
                res.append(curr.copy())
                return

            for j in range(i,len(candidates)):

                if total+candidates[j]>target:
                    return

                if j>i and candidates[j]==candidates[j-1]:
                    continue
                curr.append(candidates[j])
                backtrack(j+1,curr,total+candidates[j])
                curr.pop()

        backtrack(0,[],0)
        return res