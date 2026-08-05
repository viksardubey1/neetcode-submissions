class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        value_list = self.store[key]
        lo, hi = 0, len(value_list) - 1
        answer = ""
        while lo <= hi:
            mid = (hi + lo) // 2
            if value_list[mid][1] > timestamp:
                hi = mid - 1
            else:
                answer = value_list[mid][0]
                lo = mid + 1
        return answer

        
