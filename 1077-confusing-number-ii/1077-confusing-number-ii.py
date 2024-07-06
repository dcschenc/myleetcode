class Solution:
    def confusingNumberII(self, n: int) -> int:
        def is_confusing(n_str: int) -> bool:
            # special case - single digit
            if len(n_str)==1:
                return n_str not in {'0', '1', '8'}            
            left = 0
            right = len(n_str)-1
            while left<=right:
                if matching[n_str[left]]!=n_str[right]:
                    return True
                left+=1
                right-=1
            return False

        def backtrack(val_str, val):
            nonlocal total
            if 1 <= val <= n:
                if is_confusing(val_str):
                    total += 1
            elif val > n:
                return

            for c in matching.keys():
                if val==0:
                    if c=='0':
                        continue
                    backtrack(val_str + c, val*10 + int(c))
                # has at least 1 digit
                else: 
                    backtrack(val_str + c, val*10 + int(c))

        matching = {'1':'1', '6':'9', '9':'6', '8':'8', '0':'0'}
        total = 0
        backtrack('', 0)
        return total
