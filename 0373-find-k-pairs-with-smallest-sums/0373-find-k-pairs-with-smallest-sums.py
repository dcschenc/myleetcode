class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []  # Create a min-heap to store pairs (a, b)

        # Initialize the heap with the first k pairs (nums1[0], nums2[0..k-1])
        for i in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[i], 0, i))

        result = []
        
        while k > 0 and heap:
            sum_ab, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # If there are more pairs in nums1, add the next pair (nums1[i+1], nums2[j]) to the heap
            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            
            k -= 1

        return result

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