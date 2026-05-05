class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row where target could be
        l,r=0,len(matrix)-1
        row=None
        while l<=r:
            m=(l+r)//2
            if target<matrix[m][0]:
                r=m-1
            elif target>matrix[m][-1]:
                l=m+1
            else:
                row=matrix[m]
                break
        
        if row == None:
            return False # no viable row found
        
        # find target in row
        l,r=0,len(row)-1
        while l<=r:
            m=(l+r)//2
            if target<row[m]:
                r=m-1
            elif target>row[m]:
                l=m+1
            else:
                return True
        return False
