class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value,timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            array = self.map[key]
            hi = len(array) - 1
            lo = 0
            val = timestamp
            potential = -1
            while (lo<=hi):
                mid = lo + (hi-lo)//2
                if (val >= array[mid][1]):
                    potential = mid
                    lo = mid+1
                else:
                    hi = mid-1
            if (potential >= 0):
                return array[potential][0]
            else:
                return ""
                    
            
