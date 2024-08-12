class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # https://algo.monster/liteproblems/2826
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2826.Sorting%20Three%20Groups

        # f will hold the minimum operations required to adjust the list
        # to the constraints of having 1s, 2s and no elements in position i
        min_operations = [0] * 3

        # Loop through each element in the nums list
        for number in nums:
            # g will temporarily hold the new calculated minimum operations
            new_min_operations = [0] * 3

            # If the current number is 1
            if number == 1:
                new_min_operations[0] = min_operations[0]  # No change needed
                new_min_operations[1] = min(min_operations[:2]) + 1  # Increment operations for 1s or 2s
                new_min_operations[2] = min(min_operations) + 1  # Increment as 1 is not allowed here
            # If the current number is 2
            elif number == 2:
                new_min_operations[0] = min_operations[0] + 1  # Increment as 2 is not allowed here
                new_min_operations[1] = min(min_operations[:2])  # No change needed
                new_min_operations[2] = min(min_operations) + 1  # Increment operations for no number
            # If the current number is neither 1 nor 2
            else:
                new_min_operations[0] = min_operations[0] + 1  # Increment as number is not allowed here
                new_min_operations[1] = min(min_operations[:2]) + 1  # Increment operations for 1s or 2s
                new_min_operations[2] = min(min_operations)  # No change needed 

            # Update min_operations with the new calculated minimum operations
            min_operations = new_min_operations

        # Return the minimum of the calculated operations
        return min(min_operations)


        def get_number(i, j):
            cnt = 0
            cnt += nums[:i].count(1)
            cnt += nums[i:j].count(2)
            cnt += nums[j:n].count(3)
            return n - cnt            

        n = len(nums)
        ans = n
        for i in range(n + 1):
            for j in range(i, n + 1):
                ans = min(ans, get_number(i, j))
        return ans