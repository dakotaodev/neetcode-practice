class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # FIND ROW
        l,r=0,len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0] > target:
                r=m-1
            elif matrix[m][-1]<target:
                l=m+1
            else:
                # m is the row to search
                break
        
        # FIND TARGET IN ROW
        l,r=0,len(matrix[m])-1
        row=matrix[m]
        while l<=r:
            m=(l+r)//2
            if row[m] < target:
                l=m+1
            elif row[m]>target:
                r=m-1
            else:
                return True
        
        return False