class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups:dict[str, list]={}

        for s in strs:
            s_sorted="".join(sorted(s))
            if s_sorted in groups:
                group=groups.get(s_sorted)
                group.append(s)
                groups[s_sorted]=group
            else:
                groups[s_sorted]=[s]
        
        return list(groups.values())