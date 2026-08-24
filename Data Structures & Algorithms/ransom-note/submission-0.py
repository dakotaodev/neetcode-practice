class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count: dict[str, int] = defaultdict(int)

        for l in magazine:
            mag_count[l]+=1
        
        for l in ransomNote:
            if l in mag_count and mag_count[l] > 0:
                mag_count[l]-=1
            else:
                return False
        return True