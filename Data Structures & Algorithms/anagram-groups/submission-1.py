class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Approach
        # sort the str
        # use sorted str as key
        # add to key. value is a list 
        # return dict values as a list

        groups:dict[str, list] = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            group = groups.get(s_sorted, [])
            group.append(s)
            groups[s_sorted]=group

        return list(groups.values())