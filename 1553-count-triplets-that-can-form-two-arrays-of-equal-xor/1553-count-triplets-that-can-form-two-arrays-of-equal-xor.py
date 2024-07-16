class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
        prefix_XOR = [0] + arr[:]
        size = len(prefix_XOR)

        # Perform XOR on consecutive elements in the modified array
        for i in range(1, size):
            prefix_XOR[i] ^= prefix_XOR[i - 1]

        count = 0

        # Iterate through the modified array to count triplets
        for start in range(size):
            for end in range(start + 1, size):
                if prefix_XOR[start] == prefix_XOR[end]:
                    # Increment the result by the count of valid triplets
                    count += end - start - 1

        return count

        n, ans = len(arr), 0
        for i in range(n-1):
            a = arr[i]
            for j in range(i+1, n):
                if j != i + 1:
                    a = a ^ arr[j-1]
                b = arr[j]
                if a == b: 
                    ans += 1
                for k in range(j+1, n):
                    b = b ^ arr[k]
                    if a == b:
                        ans += 1
        return ans