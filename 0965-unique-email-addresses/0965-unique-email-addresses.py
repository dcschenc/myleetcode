class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            # print(email)
            parts = email.split('@')
            local = parts[0]
            sent = ''
            for c in local:
                if c == '+':
                    break
                elif c != '.':
                    sent += c
            # print(sent + parts[1])
            if sent + '@' + parts[1] not in res:
                res.add(sent  + '@' + parts[1])
        return len(res)