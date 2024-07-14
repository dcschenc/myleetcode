class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1356.Sort%20Integers%20by%20The%20Number%20of%201%20Bits
        return sorted(arr, key=lambda x: (x.bit_count(), x))
        
        def compare(x):
            bits = 0
            origin_x = x
            while x > 0:
                if x & 1 == 1:
                    bits += 1
                x >>= 1
            return bits, origin_x

        arr.sort(key=compare)
        return arr