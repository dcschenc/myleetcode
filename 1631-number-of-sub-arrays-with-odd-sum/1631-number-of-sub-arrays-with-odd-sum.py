class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7        
        current_sum = 0
        even_count = 1  # Initially, there is one even sum (prefix sum is 0)
        odd_count = 0
        result = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1
            
            result %= MOD
        
        return result
        
        mod = 10 ** 9 + 7
        n = len(arr)
        cur, ans = 0, 0
        odd, even = 0, 1
        for i in range(n):
            cur += arr[i]
            if cur%2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1
        return ans%mod
            