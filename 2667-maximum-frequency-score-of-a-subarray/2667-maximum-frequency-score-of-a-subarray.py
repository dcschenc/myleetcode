class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2524.Maximum%20Frequency%20Score%20of%20a%20Subarray
        # Define the modulus for the calculations as per the problem statement, which is 10^9 + 7
        mod = 10**9 + 7      
        # Create a Counter for the first 'k' elements in the list
        counter = Counter(nums[:k])
      
        # Calculate the initial score by raising 'k' to the power of the frequency count, modulo 'mod'
        current_score = sum(pow(num, frequency, mod) for num, frequency in counter.items()) % mod
      
        # Set the 'answer' to the initial score, it will keep track of the highest score
        answer = current_score
      
        # Start iterating from the 'k'th element in 'nums'
        i = k
        while i < len(nums):
            # 'previous_num' is the number which will be excluded from the current window
            # 'new_num' is the number which will be included in the current window
            previous_num, new_num = nums[i - k], nums[i]
          
            # Only process if we're examining a new number; otherwise, skip re-calculation
            if previous_num != new_num:
                # Increase the score by the power of the count of the new number, if it already exists
                current_score += (new_num - 1) * pow(new_num, counter[new_num], mod) if counter[new_num] else new_num
              
                # Decrease the score by the power of the count of the previous number, if necessary
                current_score -= (previous_num - 1) * pow(previous_num, counter[previous_num] - 1, mod) if counter[previous_num] > 1 else previous_num
              
                # Ensure the current score does not exceed 'mod'
                current_score %= mod
              
                # Update the counter for the new window
                counter[new_num] += 1
                counter[previous_num] -= 1
              
                # Update the answer if the current score is higher
                answer = max(answer, current_score)
          
            # Move to the next element
            i += 1
      
        # Return the highest score found
        return answer


        mod = 10**9 + 7
        cnt = Counter(nums[:k])
        ans = cur = sum(pow(k, v, mod) for k, v in cnt.items()) % mod
        i = k
        while i < len(nums):
            a, b = nums[i - k], nums[i]
            if a != b:
                cur += (b - 1) * pow(b, cnt[b], mod) if cnt[b] else b
                cur -= (a - 1) * pow(a, cnt[a] - 1, mod) if cnt[a] > 1 else a
                cur %= mod
                cnt[b] += 1
                cnt[a] -= 1
                ans = max(ans, cur)
            i += 1
        return ans