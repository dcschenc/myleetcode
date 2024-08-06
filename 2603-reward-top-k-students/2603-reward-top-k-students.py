from collections import defaultdict
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2512.Reward%20Top%20K%20Students
        ps = set(positive_feedback)
        ns = set(negative_feedback)
        arr = []
        for sid, r in zip(student_id, report):
            t = 0
            for w in r.split():
                if w in ps:
                    t += 3
                elif w in ns:
                    t -= 1
            arr.append((t, sid))
        arr.sort(key=lambda x: (-x[0], x[1]))
        return [v[1] for v in arr[:k]]


        # scores = defaultdict(list)
        # positive_feedback = set(positive_feedback)
        # negative_feedback = set(negative_feedback)
        # for i, r in enumerate(report):
        #     words = r.split()
        #     cur = 0
        #     for w in words:
        #         if w in positive_feedback:
        #             cur += 3
        #         if w in negative_feedback:
        #             cur -= 1
        #     scores[cur].append(student_id[i])
        # sorted_items = sorted(scores.items(), key=lambda x: x[0], reverse=True)
        # ans = []
        # for _, v in sorted_items:
        #     v.sort()
        #     for sid in v:
        #         ans.append(sid)
        #         k -= 1
        #         if k == 0:
        #             return ans
