class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # ans = [0] * num_people

        # l, i = 0, 1
        # while candies > 0:
        #     if candies < i:
        #         ans[l] += candies
        #     else:
        #         ans[l] += i
        #     candies -= i
        #     l += 1
        #     i += 1
        #     if l >= num_people:
        #         l = 0
            
        # return ans

        res = [0] * num_people
        count = 0
        while candies > 0:
            for i in range(num_people):
                cur = count * num_people + (i+1)
                if cur < candies:
                    res[i] += cur
                    candies -=  cur
                else:
                    res[i] += candies
                    return res
            count += 1
        return res