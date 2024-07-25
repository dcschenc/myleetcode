class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1826.Faulty%20Sensor
        i, n = 0, len(sensor1)
        while i < n - 1:
            if sensor1[i] != sensor2[i]:
                break
            i += 1
        while i < n - 1:   ### no need to check the last one
            if sensor1[i + 1] != sensor2[i]:
                return 1
            if sensor1[i] != sensor2[i + 1]:
                return 2
            i += 1
        return -1