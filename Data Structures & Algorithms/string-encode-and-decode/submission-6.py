class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result=result+str(len(s))+"#"+s
        return result

    def decode(self, s: str) -> List[str]:
        results=[]

        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1

            length=int(s[i:j])
        
            # move to after delimiter
            i=j+1
            j=i+length
            # get substring
            res=s[i:j]
            results.append(res)
            # move to next
            i=j   
        return results