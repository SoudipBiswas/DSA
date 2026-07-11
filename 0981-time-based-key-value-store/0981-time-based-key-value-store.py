import collections
import bisect

class TimeMap:
    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return arr[left - 1][0] if left > 0 else ""
