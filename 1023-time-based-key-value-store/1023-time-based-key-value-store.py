class TimeMap:
    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.hm:
            self.hm[key] = []
            
        # Store '(timestamp, value)' pair in 'key' bucket.
        self.hm[key].append([timestamp, value ])
        

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.hm:
            return ""
        
        if timestamp < self.hm[key][0][0]:
            return ""
        
        left = 0
        right = len(self.hm[key])
        
        while left < right:
            mid = (left + right) // 2
            if self.hm[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # If iterator points to first element it means, no time <= timestamp exists.
        return "" if right == 0 else self.hm[key][right - 1][1]
        
    # def __init__(self):
    #     self.kv = {}        

    # def set(self, key: str, value: str, timestamp: int) -> None:
    #     if key not in self.kv:
    #         self.kv[key] = [[], []]
    #     self.kv[key][0].append(timestamp)  # 0: timestamp
    #     self.kv[key][1].append(value)      # 1: value

    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.kv:
    #         return ""
    #     times = self.kv[key][0]
    #     if timestamp < times[0]:
    #         return ""
    #     left, right = 0, len(times) - 1
    #     while left < right:
    #         mid = (left + right)//2
    #         if times[mid] > timestamp:
    #             right = mid
    #         else:
    #             left = mid + 1       
    #     if times[left] <= timestamp:
    #         return self.kv[key][1][left]
    #     elif left - 1 >= 0 and times[left-1] <= timestamp:
    #         return self.kv[key][1][left-1]
    #     return ""        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)