class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1103.Distribute%20Candies%20to%20People
        ans = [0] * num_people
        i = 0
        while candies:
            ans[i % num_people] += min(candies, i + 1)
            candies -= min(candies, i + 1)
            i += 1
        return ans