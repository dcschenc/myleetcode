class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1899.Merge%20Triplets%20to%20Form%20Target%20Triplet
        x, y, z = target
        d = e = f = 0
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                d = max(d, a)
                e = max(e, b)
                f = max(f, c)
        return [d, e, f] == target
        
        a, b, c = [], [], []
        for x, y, z in triplets:
            if x == target[0] and y <= target[1] and z <= target[2]:
                a.append((x, y, z))
            if y == target[1] and x <= target[0] and z <= target[2]:
                b.append((x, y, z))
            if z == target[2] and x <= target[0] and y <= target[1]:
                c.append((x, y, z))
        return len(a) != 0 and len(b) != 0 and len(c) != 0
           
        
