class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2337.Move%20Pieces%20to%20Obtain%20a%20String
        
        # Create pairs of (character, index) for non '_' characters in start string.
        start_positions = [(char, index) for index, char in enumerate(start) if char != '_']
      
        # Create pairs of (character, index) for non '_' characters in target string.
        target_positions = [(char, index) for index, char in enumerate(target) if char != '_']
      
        # If the number of non '_' characters in start and target are different, return False.
        if len(start_positions) != len(target_positions):
            return False
      
        # Iterate over the pairs of start and target together.
        for (start_char, start_index), (target_char, target_index) in zip(start_positions, target_positions):
            # If the characters are not the same, the transformation is not possible.
            if start_char != target_char:
                return False
            # A 'L' character in start should have an index greater than or equal to that in target.
            if start_char == 'L' and start_index < target_index:
                return False
            # A 'R' character in start should have an index less than or equal to that in target.
            if start_char == 'R' and start_index > target_index:
                return False
      
        # If all conditions are met, return True indicating the transformation is possible.
        return True

