class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A,B=nums1,nums2
        if len(A)>len(B):
            A,B=B,A

        total=len(A)+len(B)
        half=total//2
        l,r=0,len(A)-1
        while True:
            i=(l+r)//2
            j=half-2-i

            AL=A[i] if i>=0 else float("-infinity")
            AR=A[i+1] if i+1<len(A) else float("infinity")
            BL=B[j] if j>=0 else float("-infinity")
            BR=B[j+1] if j+1<len(B) else float("infinity")

            if AL<=BR and BL<=AR:
                # calculate median
                if total%2==1:
                    return min(AR,BR)
                else:
                    return (max(AL,BL)+min(AR,BR))/2
            elif AL>BR:
                r=i-1
            else:
                l=i+1