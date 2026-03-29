class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        # create char freq lists
        s1_count=[0] * 26
        s2_count=[0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')]+=1
            s2_count[ord(s2[i])-ord('a')]+=1

        # count the number of current matches
        matches=0
        for i in range(26):
            if s1_count[i]==s2_count[i]:
                matches+=1
        
        # now use a sliding window of size s1 to look for permutations
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            
            # first, add r to the counts
            index=ord(s2[r])-ord('a')
            s2_count[index]+=1
            # check if this creates a match, or ruins one
            if s2_count[index]==s1_count[index]:
                matches+=1
            elif s2_count[index]==s1_count[index]+1:
                matches-=1
            
            # now, lets work on l
            index=ord(s2[l])-ord('a')
            s2_count[index]-=1
            # check if this creates a match, or ruins one
            if s2_count[index]==s1_count[index]:
                matches+=1
            elif s2_count[index]==s1_count[index]-1:
                matches-=1
            l+=1
        return matches==26









