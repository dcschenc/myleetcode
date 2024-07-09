class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/editorial/
        ones = sum(data)
        cnt_one = max_one = 0
        left = right = 0
        while right < len(data):
            # updating the number of 1's by adding the new element
            cnt_one += data[right]
            right += 1
            # maintain the length of the window to ones
            if right - left > ones:
                # updating the number of 1's by removing the oldest element
                cnt_one -= data[left]
                left += 1
            # record the maximum number of 1's in the window
            max_one = max(max_one, cnt_one)
        return ones - max_one

        ones = sum(data)
        cnt_one = max_one = 0

        # maintain a deque with the size = ones
        deque = collections.deque()
        for i in range(len(data)):
            # we would always add the new element into the deque
            deque.append(data[i])
            cnt_one += data[i]

            # when there are more than ones elements in the deque,
            # remove the leftmost one
            if len(deque) > ones:
                cnt_one -= deque.popleft()
            max_one = max(max_one, cnt_one)
        return ones - max_one