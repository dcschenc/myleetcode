class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1: return n
        idx = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[idx] = chars[i]
            idx += 1
            if j - i > 1:               
                for d in str(j - i):                    
                    chars[idx] = d
                    idx += 1                
            i = j
        return idx

        # n = len(chars)
        # # if n <= 1:
        # #     return n
        # curr = chars[0]
        # count = 1
        # idx = 1
        # for i in range(1, len(chars)):            
        #     if chars[i] != curr:                
        #         curr = chars[i]
        #         if count > 1:
        #             count_str = str(count)
        #             for c in count_str:
        #                 chars[idx] = c
        #                 idx += 1
        #         chars[idx] = curr
        #         idx +=1
        #         count = 1                
        #     else:
        #         count += 1
        
        # if count > 1:
        #     count_str = str(count)
        #     for c in count_str:
        #         chars[idx] = c
        #         idx += 1
        #     # idx +=1
        # # else:
        #     # idx +=1
        # return idx
