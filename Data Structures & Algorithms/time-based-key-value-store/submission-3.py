class TimeMap:

    def __init__(self):
        self.cache=defaultdict(list) #key : list of (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        
        values=self.cache[key]
        
        l,r=0,len(values)-1
        res=""
        while l<=r:
            m=(l+r)//2
            if values[m][1]<timestamp:
                res=values[m][0]
                l=m+1
            elif values[m][1]>timestamp:
                r=m-1
            else:
                return values[m][0]
        return res
