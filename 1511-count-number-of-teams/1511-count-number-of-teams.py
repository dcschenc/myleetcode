class Solution:
    # https://leetcode.com/problems/count-number-of-teams/solutions/724711/easiest-code-ever-python-top-97-speed-o-n-log-n-combinatorial/
    def numTeams(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        for i, b in enumerate(rating):
            l = sum(a < b for a in rating[:i])
            r = sum(c > b for c in rating[i + 1 :])
            ans += l * r
            ans += (i - l) * (n - i - 1 - r)
        return ans

        # cnt, n = 0, len(rating)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
        #                 cnt += 1
                    
        # return cnt
