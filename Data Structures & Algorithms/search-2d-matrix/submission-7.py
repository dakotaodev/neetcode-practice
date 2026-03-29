class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # find the candidate row
        l,r=0,len(matrix)-1
        row=None
        while l<=r:
            m=(r+l)//2
            if matrix[m][0]>target:
                r=m-1
            elif matrix[m][-1]<target:
                l=m+1
            else:
                row=matrix[m]
                break
        
        # find the target in the row
        if row==None:
            return False
        l,r=0,len(row)
        while l<=r:
            m=(r+l)//2
            if row[m]<target:
                l=m+1
            elif row[m]>target:
                r=m-1
            else:
                return True


        return False 