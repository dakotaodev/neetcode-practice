class TimeMap:

    def __init__(self):
        self.timemap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        v=self.timemap.get(key,[])
        v.append([value, timestamp])
        self.timemap[key]=v        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        # key exists, search for value
        result=""
        values=self.timemap[key]
        l,r=0,len(values)-1
        while l<=r:
            m=(l+r)//2
            if values[m][1] < timestamp:
                # this is a valid candidate, track and move to search for more recent
                result=values[m][0]
                l=m+1
            elif values[m][1] > timestamp:
                # invalid candidate, search lhs of search space
                r=m-1
            else:
                # the timestamp matches exactly, this is the best case
                return values[m][0]
        return result

