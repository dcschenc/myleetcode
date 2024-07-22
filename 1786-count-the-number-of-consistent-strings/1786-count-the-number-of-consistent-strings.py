class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:        
        # count = 0
        # allowed = set(allowed)
        # for w in words:
        #     consistent = True
        #     for c in w:
        #         if c not in allowed:
        #             consistent = False
        #             break
        #     if consistent:
        #         count += 1
        # return count
        
        count = 0
        allowed = set(allowed)
        for w in words:
            if all(c in allowed for c in w):
                count += 1
        return count
