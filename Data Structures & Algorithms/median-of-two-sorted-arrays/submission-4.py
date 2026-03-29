class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        
        A,B=nums1,nums2
        if len(B)<len(A):
            A,B=B,A
        
        total=len(A)+len(B)
        half=total//2

        l,r=0,len(A)-1
        while True:
            m=(l+r)//2
            i=half-m-2
            Al=A[m] if m>=0 else float("-infinity")
            Ar=A[m+1] if (m+1) < len(A) else float("infinity")
            Bl=B[i] if i>=0 else float("-infinity") 
            Br=B[i+1] if (i+1)<len(B) else float("infinity")

            if Al<=Br and Bl<=Ar:
                if total%2==1:
                    return min(Ar,Br)
                else:
                    return (max(Al,Bl)+min(Ar,Br))/2
            elif Al>Br:
                r=m-1
            else:
                l=m+1




