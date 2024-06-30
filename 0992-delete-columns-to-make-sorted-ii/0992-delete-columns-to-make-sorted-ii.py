class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # https://algo.monster/liteproblems/955
        # Check if the input list is None or has only one string; if so, no deletion is needed.
        strings = strs
        if strings is None or len(strings) <= 1:
            return 0
      
        # Initialize the number of strings and the length of the first string.
        n = len(strings)
        string_length = len(strings[0])
        deletions = 0
      
        # Initialize a list to keep track of which strings are already sorted.
        sorted_status = [False] * n
  
        # Iterate over each column by index.
        for j in range(string_length):
            # Attempt to update sorted status for this column.
            for i in range(n - 1):
                # If the current string is not sorted with the next, and the current character
                # is greater than the next string's character, we need to delete this column.
                if not sorted_status[i] and strings[i][j] > strings[i + 1][j]:
                    # Increment the deletion counter.
                    deletions += 1
                    break  # Skip to the next column without updating the sorted status.

            else: # This else belongs to the for, it is executed if the loop is not 'break'-ed.
                # Update sorted status if this column does not need to be deleted.
                for i in range(n - 1):
                    # If the characters are in ascending order, mark as sorted.
                    if strings[i][j] < strings[i + 1][j]:
                        sorted_status[i] = True
      
        # Return the total number of columns that need to be deleted.
        return deletions

        cur = 0
        n = len(strs[0])
        while cur < n:
            # if all(a[cur] <= b[cur] for a, b in pairwise(strs)):
            #     return cur
            delete = False
            for i in range(1, n):
                if strs[i-1][cur] < strs[i][cur] or strs[i-1][cur] == strs[i][cur] and strs[i-1][cur + 1] <= strs[i][cur + 1]:
                    continue
                else:                   
                    delete = True
                    break
            if delete is False:
                return cur
            else:
                cur += 1
        return cur