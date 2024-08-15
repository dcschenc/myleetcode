# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
        start, cnt = 0, 0
        buff = []
        while True:            
            ch = stream.next()
            if ch == pattern[cnt]:
                buff.append(ch)
                cnt += 1
                if cnt == len(pattern):
                    return start
            else:                
                buff.append(ch)
                while len(buff) > 0:
                    start += 1
                    buff = buff[1:]
                    cnt = len(buff)
                    if buff == pattern[:cnt]:
                        break