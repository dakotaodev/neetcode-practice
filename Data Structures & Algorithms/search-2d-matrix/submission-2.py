class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find the candidate row
        l=0
        r=len(matrix)-1
        row=None
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]>target:
                r=m-1
            elif matrix[m][-1]<target:
                l=m+1
            else:
                row=matrix[m]
                break
        if not row:
            return False
        # search the row
        l=0
        r=len(row)-1
        while l<=r:
            m=(l+r)//2
            if row[m]<target:
                l=m+1
            elif row[m]>target:
                r=m-1
            else:
                return True
        return False