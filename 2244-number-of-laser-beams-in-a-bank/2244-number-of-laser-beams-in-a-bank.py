class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2125.Number%20of%20Laser%20Beams%20in%20a%20Bank
        n = len(bank)
        i = 0
        prev_ones = 0
        total = 0
        for i, devices in enumerate(bank):
            ones = devices.count('1')
            total += prev_ones * ones
            if ones != 0:
                prev_ones = ones
        return total
