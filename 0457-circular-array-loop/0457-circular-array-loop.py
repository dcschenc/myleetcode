class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            slow, fast = i, i
            isPositive = True if nums[i] > 0 else False
            while True:
                slow = (slow + nums[slow])%n   
                if (nums[slow] > 0) != isPositive:
                    break                
                fast = (fast + nums[fast])%n
                if (nums[fast] > 0) != isPositive:
                    break
                fast = (fast + nums[fast])%n
                if slow == fast:
                    if (slow + nums[slow])%n == slow:
                        break
                    return True
            j = i
            while nums[j] > 0:
                tmp = nums[j]
                nums[j] = 0
                j = (tmp + j)%n
        return False           


    # def circularArrayLoop(self, nums):
    #     n = len(nums)
        
    #     for i in range(n):
    #         if nums[i] == 0:
    #             continue            
    #         slow = i
    #         fast = i
    #         is_forward = nums[i] > 0  # Check the direction of the loop
            
    #         while True:
    #             slow = (slow + nums[slow]) % n
    #             if (nums[slow] > 0) != is_forward:
    #                 break  # Invalid loop (direction mismatch)
                
    #             fast = (fast + nums[fast]) % n
    #             if (nums[fast] > 0) != is_forward:
    #                 break  # Invalid loop (direction mismatch)
                
    #             fast = (fast + nums[fast]) % n  # Move fast pointer two steps
                
    #             if slow == fast:
    #                 # Check if the loop length is greater than 1
    #                 if slow == (slow + nums[slow]) % n:
    #                     break  # Loop length is 1, not a valid loop
    #                 return True

    #         # Mark the elements as visited to avoid unnecessary calculations
    #         j = i
    #         while nums[j] > 0:
    #             temp = (j + nums[j]) % n
    #             nums[j] = 0
    #             j = temp

    #     return False