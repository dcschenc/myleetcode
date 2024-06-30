class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        hm = {}
        for log in logs:
            arr = log.split(' ')
            key = arr[0]
            s = ''.join(arr[1:])           
            isdigit = all(c.isdigit() for c in s)               
            if isdigit:
                digit_logs.append(log)
            else:
                letter_logs.append((key, ' '.join(arr[1:])))
        sorted_items = sorted(letter_logs, key = lambda x: (x[1], x[0]))
        result = []
        for k, v in sorted_items:
            result.append(k + ' ' + v)
        result.extend(digit_logs)
        return result