class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        change = {str(i): str(change[i]) for i in range(len(change))}
        num = list(num)
        i, n = 0, len(num)
        while i < n:            
            if change[num[i]] > num[i]:
                num[i] = change[num[i]]
                j = i + 1
                while j < n:
                    if change[num[j]] >= num[j]:
                        num[j] = change[num[j]]
                    else:
                        break
                    j += 1
                return ''.join(num)
            i += 1
        return ''.join(num)