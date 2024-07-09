class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            cnt = Counter(s)
            return next(cnt[c] for c in ascii_lowercase if cnt[c])

        n = len(words)
        nums = sorted(f(w) for w in words)
        return [n - bisect_right(nums, f(q)) for q in queries]
        
        # def compute_f(w):
        #     w = sorted(w)
        #     cnt = 1
        #     for i in range(1, len(w)):
        #         if w[i] != w[0]:
        #             break
        #         cnt += 1
        #     return cnt

        # words_f = []
        # for w in words:
        #     words_f.append(compute_f(w))
        # words_f.sort()
        # ans = []
        # for q in queries:
        #     f = compute_f(q)           
        #     left, right = 0, len(words_f)
        #     while left < right:
        #         mid = (left + right)//2
        #         if words_f[mid] > f:
        #             right = mid 
        #         elif words_f[mid] <= f:
        #             left = mid + 1
        #     ans.append(len(words_f) - left)
        # return ans
