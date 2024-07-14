class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # curr = sum(arr[:k-1])
        cur = 0
        count = 0
        left = 0
        for i in range(len(arr)):  
            cur += arr[i]  
            if i+1 >= k:
                if cur/k >= threshold:
                    count += 1
                cur -= arr[left]
                left += 1                   
        return count