class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dict_ = defaultdict(int)
#         for val in nums:
#             dict_[val] += 1
#         tmp = list(dict_.items())
#         # print(tmp)
#         tmp.sort(key=lambda x: x[1], reverse=True)
#         # print(tmp)
#         return [x[0] for x in tmp[:k]]

        # The bucket sort-based approach has a time complexity of O(n), where n is the number of elements in the input array. It can be more efficient than the min heap approach when k is significantly smaller than the number of distinct elements in the array, as it avoids the overhead of maintaining a min heap.
        
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # Step 1: Create a frequency dictionary
            counts = collections.Counter(nums)
    
            # Create a list to represent buckets, where each index corresponds to a frequency
            bucket = [[] for _ in range(len(nums) + 1)]
            
            # Place each number in the corresponding bucket
            for num, count in counts.items():
                bucket[count].append(num)
            
            # Flatten the bucket list (concatenate lists in reverse order)
            result = []
            for freq in range(len(bucket) - 1, -1, -1):
                result.extend(bucket[freq])
                if len(result) >= k:
                    break
            
            return result[:k]

           # Step 1: Create a dictionary to count frequencies
            freq_dict = collections.Counter(nums)
            
            # Step 2: Initialize a priority queue (min heap)
            min_heap = []
            
            # Step 3: Iterate through the dictionary and add elements to the heap
            for num, freq in freq_dict.items():
                if len(min_heap) < k:
                    heapq.heappush(min_heap, (freq, num))
                else:
                    if freq > min_heap[0][0]:
                        heapq.heappop(min_heap)
                        heapq.heappush(min_heap, (freq, num))
            
            # Step 7: Extract elements from the heap in reverse order
            result = []
            while min_heap:
                result.append(heapq.heappop(min_heap)[1])
            
            return result   