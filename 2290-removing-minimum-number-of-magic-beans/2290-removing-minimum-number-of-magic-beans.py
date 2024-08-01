class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2171.Removing%20Minimum%20Number%20of%20Magic%20Beans
        beans.sort()
        total_beans = sum(beans)
        min_removal = float('inf')
        n = len(beans)
        
        for i in range(n):
            # Number of beans to remove if we make all bags have beans[i] beans
            removal = total_beans - (beans[i] * (n - i))
            min_removal = min(min_removal, removal)
        
        return min_removal

        # beans.sort()
        # n, s = len(beans), sum(beans) 
        # return min(s - bag*(n - i) for i, bag in enumerate(beans))

# If you sort the bags of beans, the cost of making all the bags the same size as beans[i] is:

# The sum of beans[j], 0 <= j < i (to make all these bags empty) plus

# the sum of beans[k], i <= k < n, minus (beans[i] * (n - i)) (to make all these bags have beans[i] beans)