class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_count = defaultdict(int)
        total_pairs = 0
        
        # Step 1: Calculate gcd(nums[i], k) for each number and populate gcd_count
        for num in nums:
            g = gcd(num, k)
            gcd_count[g] += 1
        
        # Step 2: Iterate over all pairs of gcds and count valid pairs
        gcd_keys = list(gcd_count.keys())
        for i in range(len(gcd_keys)):
            for j in range(i, len(gcd_keys)):
                g1, g2 = gcd_keys[i], gcd_keys[j]
                # Check if g1 * g2 is divisible by k
                if (g1 * g2) % k == 0:
                    if i == j:
                        # If g1 == g2, choose pairs from the same group
                        total_pairs += gcd_count[g1] * (gcd_count[g1] - 1) // 2
                    else:
                        # Count cross pairs between different gcd groups
                        total_pairs += gcd_count[g1] * gcd_count[g2]
        
        return total_pairs