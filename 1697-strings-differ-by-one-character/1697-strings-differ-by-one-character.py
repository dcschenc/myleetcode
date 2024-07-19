class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        # for i in range(len(dict[0])):
        #     all_opt = set()
        #     for w in dict:
        #         w1 = w[:i] + '*' + w[i+1:]
        #         if w1 in all_opt:
        #             return True
        #         all_opt.add(w1)
        # return False
        
        for i in range(len(dict[0])):
            seen = set()
            for s in dict:            
                key = s[:i] + '*' + s[i+1:]
                if key in seen:
                    return True
                seen.add(key)
        return False

        # set_dict = set(dict)
        # for s in dict:
        #     for i in range(len(s)):
        #         for c in 'abcdefghijklmnokprstuvwxyz':
        #             if s[i] != c and  s[:i] + c + s[i+1:] in set_dict:
        #                 return True
        # return False
