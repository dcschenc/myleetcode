class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1583.Count%20Unhappy%20Friends
        
        # Create a dictionary to store preferences index for quick lookup.
        # `preference_rankings` is a list of dictionaries for each person,
        # mapping their friend to the ranking of that friend in their preference.
        preference_rankings = [{friend: rank for rank, friend in enumerate(prefs)} for prefs in preferences]
      
        # Create a dictionary to store each person's paired friend.
        paired_friends = {}
        for x, y in pairs:
            paired_friends[x] = y
            paired_friends[y] = x
      
        # Initialize the count of unhappy friends.
        unhappy_count = 0
      
        # Iterate through each person to determine if they are unhappy.
        for x in range(n):
            # The paired friend of `x`.
            y = paired_friends[x]
          
            # Check if there exists a person 'u' who is a better preference for 'x'
            # than 'x's paired friend 'y'. We do this by checking the preference
            # rankings in the subset of preferences before 'y'.
            is_unhappy = any(
                preference_rankings[u][x] < preference_rankings[u][paired_friends[u]] # paired_friends[u]: v
                for u in preferences[x][: preference_rankings[x][y]]
            )
          
            # If such a person 'u' exists, increment the unhappy count.
            if is_unhappy:
                unhappy_count += 1
      
        return unhappy_count
