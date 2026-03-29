class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result+=str(len(s))+"#"+s
        return result

    def decode(self, s: str) -> List[str]:
        results=[]
        i=0

        while i<len(s):
            # capture the length
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            # get the string
            i=j+1
            res=s[i:i+length]
            results.append(res)
            # move to the next string
            i=i+length
        
        return results
