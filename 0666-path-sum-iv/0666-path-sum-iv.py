class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # Helper function for depth-first search from a given node with cumulative total `total`
        def dfs(node, total):
            nonlocal answer
            # If the current node is not in the tree, stop the recursion
            if node not in tree_map:
                return
            # Add the current node's value to the running total
            total += tree_map[node]
            depth, pos = divmod(node, 10) # Split the node code into depth and positional information
            # Calculate the node code for the left and right children
            left_child = (depth + 1) * 10 + (pos * 2) - 1
            right_child = left_child + 1
            # If both children are absent, add the current total to the global 'answer'
            if left_child not in tree_map and right_child not in tree_map:                
                answer += total
                return
            # Recurse on the left and right children
            dfs(left_child, total)
            dfs(right_child, total)

        # Initialize the answer variable to accumulate the total path sums
        answer = 0
        # Create a mapping from node codes (depth and position) to values using list comprehension
        tree_map = {num // 10: num % 10 for num in nums}
        # Start the DFS traversal from the root node (code 11) with an initial total of 0
        dfs(11, 0)
        # Return the accumulated total path sums
        return answer



        # def get_digits(num):
        #     level = num // 100
        #     pos = (num // 10) % 10
        #     d = num % 10
        #     return level, pos, d

        # prev_level = 0
        # prev_hm = defaultdict(int)
        # cur_hm = defaultdict(int)
        # total = 0
        # parents = set()
        # for num in nums:
        #     level, pos, d = get_digits(num)
        #     if level != prev_level:
        #         for k, v in prev_hm.items():
        #             if k not in parents:
        #                 total += v
        #         parents = set()
        #         prev_hm = cur_hm.copy()
        #         cur_hm = defaultdict(int)                
        #         prev_level = level
        #     prev_pos = math.ceil(pos/2)
        #     d += prev_hm[prev_pos]
        #     parents.add(prev_pos)
        #     cur_hm[pos] = d

        # for k, v in prev_hm.items():
        #     if k not in parents:
        #         total += v
        # for k, v in cur_hm.items():
        #     total += v
        # return total
            
         
