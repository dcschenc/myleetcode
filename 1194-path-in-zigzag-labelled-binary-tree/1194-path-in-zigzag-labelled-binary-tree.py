class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1104.Path%20In%20Zigzag%20Labelled%20Binary%20Tree        
        level_start_value = level_index = 1

        # Determine the level of the tree where the label is. The levels in the tree
        # double in number each time (1, 2, 4, 8, ...), hence the use of bit shifting
        # to represent this binary progression. The level_index keeps track of the depth.
        while (level_start_value << 1) <= label:
            level_start_value <<= 1
            level_index += 1

        # Initialize an array to store the path from the root to the label
        path = [0] * level_index

        # Working back up the tree from the label to the root
        while level_index:
            # Set the current position in the path array to the label
            path[level_index - 1] = label
            # Calculate the label's parent in the next higher level.
            # Zigzag pattern means we have to invert the label within its level
            label = ((1 << (level_index - 1)) + (1 << level_index) - 1 - label) >> 1
            level_index -= 1
      
        # Return the path that was constructed
        return path
