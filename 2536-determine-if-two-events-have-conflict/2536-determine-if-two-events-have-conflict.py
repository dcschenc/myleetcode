class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2446.Determine%20if%20Two%20Events%20Have%20Conflict

        return not (event1[0] > event2[1] or event1[1] < event2[0])

        return not (event1[0] < event2[0] and event1[1] < event2[0] or event1[0] > event2[0] and event1[0] > event2[1])
