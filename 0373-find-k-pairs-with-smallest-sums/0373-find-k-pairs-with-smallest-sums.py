class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # https://leetcode.com/problems/find-k-pairs-with-smallest-sums/editorial/
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        while k > 0 and minHeap:
            val, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1
        
        return ans
        # m, n = len(nums1), len(nums2)
        # mat = [[0] * n for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         mat[i][j] = nums1[i] + nums2[j]
        # res = []
        # i, j = 0, 0
        # ii, jj = 1, 0
        # print(mat)
        # while k > 0:     
        #     if i == m-1:
        #         res.append([nums1[i], nums2[j]])
        #         j += 1
        #         if j == n:
        #             break
        #     elif mat[i][j] <= mat[ii][jj]:
        #         res.append([nums1[i], nums2[j]])
        #         j += 1
        #         if j == n:
        #             i = ii
        #             j = jj
        #             ii = i+1
        #             jj = 0
        #     else:
        #         res.append([nums1[ii], nums2[jj]])
        #         jj += 1
        #         if jj == n:
        #             ii += 1
        #             jj = 0
        #     k -= 1
        # print(res)
        # return res