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
            # get the length
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            # parse the string
            i=j+1
            j=i+length
            results.append(s[i:j])
            # move i
            i=j
        return results