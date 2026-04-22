class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res=res+str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]

        i=0
        while i<len(s):
            # FIND LENGTH
            j=i
            while s[j] != "#":
                j+=1
            length=int(s[i:j])
            # PARSE STR
            i=j+1
            res.append(s[i:i+length])
            # MOVE POINTERS
            i=i+length

        return res