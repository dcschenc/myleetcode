class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0948.Bag%20of%20Tokens
        left, right, score = 0, len(tokens) - 1, 0
        tokens.sort()

        while left <= right:
            # When we have enough power, play lowest token face-up
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1

            # We don't have enough power to play a token face-up
            # If there is at least one token remaining,
            # and we have enough score, play highest token face-down
            elif left < right and score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            # We don't have enough score, power, or tokens 
            # to play face-up or down and increase our score
            else:
                return score

        return score       

        # tokens.sort()
        # i, j = 0, len(tokens) - 1
        # ans = t = 0
        # while i <= j:
        #     if power >= tokens[i]:
        #         power -= tokens[i]
        #         i, t = i + 1, t + 1
        #         ans = max(ans, t)
        #     elif t:
        #         power += tokens[j]
        #         j, t = j - 1, t - 1
        #     else:
        #         break
        # return ans

        # if len(tokens) == 0 or power < min(tokens):
        #     return 0
        # tokens.sort(reverse=True)       
        # power = power - tokens[-1]        
        # tokens = tokens[:-1]
        # total = sum(tokens)
        # i, n = 0, len(tokens)
        # while power < total:
        #     power += tokens[i]
        #     total -= tokens[i]
        #     i += 1
        # return n - i if n != i else 1