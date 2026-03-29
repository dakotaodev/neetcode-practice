class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row
        l,r=0,len(matrix)-1
        row=None
        while l<=r:
            m=(l+r)//2
            if matrix[m][-1]<target:
                l+=1
            elif matrix[m][0]>target:
                r-=1
            else:
                row=matrix[m]
                break
        if not row:
            return False
        
        # find in the row
        l,r=0, len(row)-1
        while l<=r:
            m=(l+r)//2
            if row[m]<target:
                l+=1
            elif row[m]>target:
                r-=1
            else:
                return True
        
        return False