class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block_comment = False
        current_line = ""

        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if not in_block_comment and i + 1 < n and line[i:i + 2] == "//":
                    break
                elif not in_block_comment and i + 1 < n and line[i:i + 2] == "/*":
                    in_block_comment = True
                    i += 1
                elif in_block_comment and i + 1 < n and line[i:i + 2] == "*/":
                    in_block_comment = False
                    i += 1
                elif not in_block_comment:
                    current_line += line[i]
                i += 1
            if current_line and not in_block_comment:
                result.append(current_line)
                current_line = ""

        return result

        ans = []
        in_block = False
        for line in source:
            if in_block is True:
                block_c = line.find('*/')
                if block_c != -1:
                    if block_c + 2 != len(line):
                        ans.append(line[block_c+2:])
                    in_block = False                
            else:
                line_c = line.find('//')
                block_c = line.find('/*')
                if line_c != -1 and block_c != -1:
                    if line_c < block_c:
                        ans.append(line[:line_c])
                    else:
                        in_block = True
                        block_d = line.find('*/')
                        if block_d > block_c:
                            in_block = False
                            if block_d + 2 < len(line):
                                ans.append(line[block_d:])
                elif line_c != -1:
                    ans.append(line[:line_c])
                elif block_c != -1:
                    in_block = True
                    if block_c != 0:
                        ans.append(line[:block_c])
                    block_d = line.find('*/')
                    if block_d > block_c:
                        in_block = False
                        if block_d + 2 < len(line):
                            ans.append(line[block_d:])
                else:
                    ans.append(line)
        return ans

