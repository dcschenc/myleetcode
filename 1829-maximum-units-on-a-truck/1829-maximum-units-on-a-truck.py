class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1710.Maximum%20Units%20on%20a%20Truck
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        total = 0
        for x, y in boxTypes:
            if x < truckSize:
                truckSize -= x 
                total += y * x
            else:
                total += y * truckSize
                break
        return total