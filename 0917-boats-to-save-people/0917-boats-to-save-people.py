class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats, left, right = 0, 0, len(people) - 1
        # print(people)
        while left <= right:
            if left == right:
                left += 1

            elif people[left] + people[right] <= limit:                
                left += 1
                right -= 1                
            else:
                left += 1
            boats += 1
        return boats