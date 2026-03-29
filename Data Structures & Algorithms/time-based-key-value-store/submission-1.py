class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            # run binary search
            values=self.map[key]
            l,r=0,len(values)-1
            result=""
            while l<=r:
                m=(l+r)//2
                if values[m][1]>timestamp:
                    r=m-1
                elif values[m][1]<timestamp:
                    result=values[m][0]
                    l=m+1
                else:
                    return values[m][0]
            return result
                    