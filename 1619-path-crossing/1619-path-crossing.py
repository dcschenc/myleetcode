class Solution:
    def isPathCrossing(self, path: str) -> bool:
        i = j = 0
        seen = {(0, 0)}
        for c in path:
            match c:
                case 'N':
                    i -= 1
                case 'S':
                    i += 1
                case 'E':
                    j += 1
                case 'W':
                    j -= 1
            if (i, j) in seen:
                return True
            seen.add((i, j))
        return False


        ctn_n, ctn_e = 0, 0
        seen = set()
        seen.add((0, 0))
        for c in path:
            if c == 'N':
                ctn_n += 1
            elif c == 'S':
                ctn_n -= 1
            elif c == 'E':
                ctn_e += 1
            else:
                ctn_e -= 1
            # print(ctn_n, ctn_e)
            if (ctn_n, ctn_e) in seen:            
                return True
            else:
                seen.add((ctn_n, ctn_e))
        return False