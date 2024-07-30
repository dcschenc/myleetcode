class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2107.Number%20of%20Unique%20Flavors%20After%20Sharing%20K%20Candies
        cnt = Counter(candies[k:])
        ans = len(cnt)
        for i in range(k, len(candies)):
            cnt[candies[i - k]] += 1
            cnt[candies[i]] -= 1
            if cnt[candies[i]] == 0:
                cnt.pop(candies[i])
            ans = max(ans, len(cnt))
        return ans
        
        # n = len(candies)
        # counter = Counter(candies)
        # total_flavor = len(counter)
        # i = 0
        # while i < k:
        #     c = candies[i]
        #     counter[c] -= 1
        #     if counter[c] == 0:
        #         counter.pop(c)
        #     i += 1    
        # ans = 0        
        # while i < n:
        #     ans = max(ans, len(counter))
        #     c = candies[i]           
        #     counter[c] -= 1
        #     if counter[c] == 0:
        #         counter.pop(c)                
        #     prev_c = candies[i-k]
        #     if prev_c in counter:
        #         counter[prev_c] += 1
        #     else:
        #         counter[prev_c] = 1
        #     i += 1
        # ans = max(ans, len(counter))
        # return ans

