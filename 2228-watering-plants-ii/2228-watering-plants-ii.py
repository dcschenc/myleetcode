class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2105.Watering%20Plants%20II
        a, b, n = capacityA, capacityB, len(plants)
        left, right = 0, n - 1
        ans, cur_a, cur_b = 0, a, b
        while left < right:
            if plants[left] > cur_a:
                cur_a = a
                ans += 1
            if plants[right] > cur_b:
                cur_b = b
                ans += 1

            if plants[left] <= cur_a:
                cur_a -= plants[left]
                left += 1                

            if plants[right] <= cur_b:
                cur_b -= plants[right] 
                right -= 1
                
        
        if n % 2 == 1 and  plants[left] > max(cur_a, cur_b):
            ans += 1
        return ans
        

        