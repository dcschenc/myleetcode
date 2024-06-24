class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            arr = queryIP.split('.')
            if len(arr) != 4:
                return 'Neither'
            for s in arr:
                if len(s) == 0 or s[0] == '0' and len(s) != 1:
                    return 'Neither'
                else:
                    for c in s:
                        if not c.isdigit():
                            return 'Neither'
                    if int(s) > 255:
                        return 'Neither'
            return 'IPv4'
        elif ':' in queryIP:
            arr = queryIP.split(':')
            if len(arr) != 8:
                return 'Neither'
            for s in arr:
                if len(s) == 0 or len(s) > 4:
                    return 'Neither'
                for c in s:
                    if not (c.isdigit() or 'a' <= c <= 'f' or 'A' <= c <= 'F'):
                        return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'