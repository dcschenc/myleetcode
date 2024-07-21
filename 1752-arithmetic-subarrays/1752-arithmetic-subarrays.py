class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n = len(l)
        # for i in range(n):
        for left, right in zip(l, r):
            # left, right = l[i], r[i]
            cur = nums[left: right + 1]            
            ans.append(True)
            if len(cur) >= 2:
                cur.sort()
                diff = cur[1] - cur[0]
                for i in range(2, len(cur)):
                    if cur[i] - cur[i-1] != diff:
                        ans[-1] = False
                        break
        return ans

                
