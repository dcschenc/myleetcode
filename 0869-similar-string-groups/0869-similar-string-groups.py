class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # https://algo.monster/liteproblems/839
        def find_leader(member):
            # Recursively find the leader for the current member
            # and perform path compression along the way.
            if parent[member] != member:
                parent[member] = find_leader(parent[member])
            return parent[member]

        # Get the total number of strings and the length of each string.
        num_strings = len(strs)
        length_of_strings = len(strs[0])

        # Initialize the parent array for union-find structure.
        parent = list(range(num_strings))

        # Compare every pair of strings in the array.
        for i in range(num_strings):
            for j in range(i + 1, num_strings):
                # Count the differences between two strings and
                # connect them if they have at most 2 differences.
                if sum(strs[i][k] != strs[j][k] for k in range(length_of_strings)) <= 2:
                    # Union of the sets that contain i and j
                    # by assigning the leader of i’s set to the leader of j's set.
                    parent[find_leader(i)] = find_leader(j)

        # Count the number of unique sets by checking the number of nodes
        # that are their own leader.
        return sum(i == find_leader(i) for i in range(num_strings))