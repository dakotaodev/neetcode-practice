class TimeMap:

    def __init__(self):
        self.cache=defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
       self.cache[key].append((value, timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        res=""
        if key in self.cache:
            values=self.cache[key]
            l,r=0,len(values)-1
            while l<=r:
                m=(l+r)//2
                curr=values[m]
                if curr[1]<timestamp:
                    res=curr[0]
                    l=m+1
                elif curr[1]>timestamp:
                    r=m-1
                else:
                    return curr[0]

        return res