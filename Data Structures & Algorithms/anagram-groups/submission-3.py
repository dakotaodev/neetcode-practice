class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}

        for s in strs:
            s_sorted="".join(sorted(s))
            g=groups.get(s_sorted, [])
            g.append(s)
            groups[s_sorted]=g
        
        return list(groups.values())