class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/editorial/
        prefix_XOR = [0] + arr[:]
        n = len(prefix_XOR)

        # Perform XOR on consecutive elements in the modified array
        for i in range(1, n):
            prefix_XOR[i] ^= prefix_XOR[i - 1]

        count = 0

        # Iterate through the modified array to count triplets
        for start in range(n):
            for end in range(start + 1, n):
                if prefix_XOR[start] == prefix_XOR[end]:
                    count += end - start - 1
        return count
