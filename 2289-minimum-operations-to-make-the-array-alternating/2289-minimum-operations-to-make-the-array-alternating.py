class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2170.Minimum%20Operations%20to%20Make%20the%20Array%20Alternating
        def f(i: int) -> Tuple[int, int, int, int]:
            k1 = k2 = 0
            cnt = Counter(nums[i::2])
            for k, v in cnt.items():
                if cnt[k1] < v:
                    k2, k1 = k1, k
                elif cnt[k2] < v:
                    k2 = k
            return k1, cnt[k1], k2, cnt[k2]

        a, b = f(0), f(1)
        n = len(nums)
        if a[0] != b[0]:
            return n - (a[1] + b[1])
        return n - max(a[1] + b[3], a[3] + b[1])


        # n, ans = len(nums), 0
        # if n == 1: return 0
        # odd = Counter([nums[i] for i in range(0, n, 2)])
        # even = Counter([nums[i] for i in range(1, n, 2)])
        # odd = sorted(odd.items(), key=lambda x:-x[1])
        # even = sorted(even.items(), key=lambda x:-x[1])
        # if len(odd) == 1 and len(even) == 1:
        #     if odd[0][0] == even[0][0]:
        #         return n//2                  
        # mx = 0
        # for i in range(len(odd)):
        #     for j in range(len(even)):
        #         if odd[i][0] != even[j][0]:
        #             mx = max(mx, odd[i][1] + even[j][1])
        #             break
        # return (n - mx)

        # for i in range(2, n):
        #     if nums[i] != nums[i-2]:
        #         nums[i] = nums[i-2]
        #         ans += 1
        # return ans