class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # https://algo.monster/liteproblems/659
        
        # Create a dictionary to map numbers to a list of sequence lengths
        sequence_lengths = defaultdict(list)

        # Iterate through all numbers in the provided list
        for num in nums:
            # If there exists a sequence ending with a number one less than the current number
            if sequence_lengths[num - 1]:
                # Pop the shortest sequence that ends with num - 1
                shortest_sequence = heappop(sequence_lengths[num - 1])
                # Add the current number to this sequence (incrementing its length)
                heappush(sequence_lengths[num], shortest_sequence + 1)
            else:
                # Start a new sequence with the current number (with length 1)
                heappush(sequence_lengths[num], 1)

        for sequence in sequence_lengths.values():
            if len(sequence) > 0 and sequence[0] <= 2:
                return False
        return True

        # Check all the (non-empty) sequences in the dictionary
        return all(len(sequence) == 0 or (len(sequence) > 0 and sequence[0] > 2) for sequence in sequence_lengths.values())

        # # the frequency of each number
        # freq = Counter(nums)
        # # the number of consecutive subsequences ending at that number
        # end = Counter()
        # # iterates through the array and tries to extend existing subsequences or create new ones.
        # for num in nums:
        #     if freq[num] == 0:
        #         continue
        #     elif end[num] > 0:
        #         end[num] -= 1
        #         end[num + 1] += 1
        #     elif freq[num + 1] > 0 and freq[num + 2] > 0:
        #         freq[num + 1] -= 1
        #         freq[num + 2] -= 1
        #         end[num + 3] += 1
        #     else:
        #         return False
        #     freq[num] -= 1
        # return True