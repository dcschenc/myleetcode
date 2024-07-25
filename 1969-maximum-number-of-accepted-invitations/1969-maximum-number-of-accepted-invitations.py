class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        # https://algo.monster/liteproblems/1820
        # Helper function to find a match for a person from "group A"
        def can_invite(boy):
            for girl_index, has_relation in enumerate(grid[boy]):
                # Check if the current person from "group B" has not been visited and there's a relation
                if has_relation and girl_index not in visited:
                    visited.add(girl_index)
                  
                    # If the person from "group B" is not matched or can be matched to another person (that means, the person that are matched now can find another to match)
                    if matches[girl_index] == -1 or can_invite(matches[girl_index]):
                        # Match person_from_a with colleague_index from "group B"
                        matches[girl_index] = boy
                        return True

            # Return False if no match is found for person_from_a
            return False

        # Number of people in "group A" and "group B" (rows and columns of the grid)
        num_boys, num_girls = len(grid), len(grid[0])
      
        # Initialize matches for each person in "group B" to -1 (indicating no matches)
        matches = [-1] * num_girls
      
        # Total number of matches (invitations) we can make
        total_invitations = 0
      
        # Loop through each person in "group A" to find a matching person in "group B"
        for boy in range(num_boys):
            # Set of visited indices in "group B" for the current person from "group A"
            visited = set()
          
            # If a match is found, increment the total number of invitations
            if can_invite(boy):
                total_invitations += 1

        # Return the total number of invitations
        return total_invitations


        # # Function to perform DFS and find an augmenting path
        # def dfs(boy):
        #     for girl in range(m):
        #         if grid[boy][girl] and not visited[girl]:
        #             visited[girl] = True
        #             if match_girl[girl] == -1 or dfs(match_girl[girl]):
        #                 match_girl[girl] = boy
        #                 match_boy[boy] = girl
        #                 return True
        #     return False

        # n = len(grid)
        # m = len(grid[0])
        
        # # Boy to girl matching array and girl to boy matching array
        # match_boy = [-1] * n
        # match_girl = [-1] * m
        # # Count of maximum matching
        # max_matching = 0
        # for boy in range(n):
        #     visited = [False] * m
        #     if dfs(boy):
        #         max_matching += 1

        # return max_matching


        # def backtrack(idx, path):
        #     ans[0] = max(ans[0], len(path))
        #     if idx == m:          
        #         return
        #     for j in range(n):
        #         if grid[idx][j] == 1 and j + 1 not in path:
        #             backtrack(idx + 1, path + [j+1])
        #     backtrack(idx + 1, path)

        # ans, m, n = [0], len(grid), len(grid[0])
        # backtrack(0, [])
        # return ans[0]
