from collections import defaultdict
class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1366.Rank%20Teams%20by%20Votes
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        cnt = defaultdict(lambda: [0] * n)
        for vote in votes:
            for i, c in enumerate(vote):
                cnt[c][i] += 1
        return "".join(sorted(votes[0], key=lambda x: (cnt[x], -ord(x)), reverse=True))

        
        # if not votes:
        #     return ""

        # team_count = len(votes[0])
        # team_positions = defaultdict(lambda: [0] * team_count)

        # for vote in votes:
        #     for i, team in enumerate(vote):
        #         team_positions[team][i] -= 1

        # sorted_teams = sorted(team_positions.keys(), key=lambda x: (team_positions[x], x))

        # return ''.join(sorted_teams)


        # hm = defaultdict(str)
        # base = ord('a')
        # for i, v in enumerate(votes):
        #     for j, c in enumerate(v):
        #         hm[c] += chr(j + base)
        
        # for k in hm.keys():
        #     hm[k] = ''.join(sorted(hm[k]))        
        # sorted_items = sorted(hm.items(), key=lambda x: (x[1], x[0]))
        # return ''.join([k for k, v in sorted_items])