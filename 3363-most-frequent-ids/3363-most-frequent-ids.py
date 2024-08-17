class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        # https://leetcode.com/problems/most-frequent-ids/solutions/4919924/easy-simple-and-optimal-solution-in-python/
        hm = defaultdict(int)
        ans = []
        heap = []
        for i in range(len(nums)):
            hm[nums[i]] += freq[i]            
            heappush(heap,(-hm[nums[i]], nums[i]))
            while -heap[0][0]!= hm[heap[0][1]]:
                heappop(heap)
            ans.append(-heap[0][0])
            
        return ans
