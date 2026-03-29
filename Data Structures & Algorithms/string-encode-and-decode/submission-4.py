class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res=res+str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        results=[]
        i=0
        while i<len(s):
            j=i
            # search for delimeter
            while s[j]!="#":
                j+=1
            # delimeter found, grab the lengeth
            length=int(s[i:j])
            # now, grab length chars are the original word
            i=j+1
            word=s[i:i+length]
            results.append(word)
            # move to next work
            i=i+length
        return results

