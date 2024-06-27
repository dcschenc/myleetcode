class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate_chars = Counter(c.lower() for c in licensePlate if c.isalpha())
        shortest_word = None
        min_length = float('inf')

        for word in words:
            word_chars = Counter(word.lower())            
            valid = all(word_chars[c] >= plate_chars[c] for c in plate_chars)      
                  
            if valid and len(word) < min_length:
                min_length = len(word)
                shortest_word = word

        return shortest_word
        
        # base_dict = defaultdict(int)
        # for c in licensePlate:
        #     if c.isalpha():                
        #         base_dict[c.lower()] += 1
        # # print(base_dict)
        # res = ''
        # min_l = 1001
        # for word in words:
        #     w_dict = defaultdict(int)
        #     for c in word:    
        #         w_dict[c] += 1
        #     competing = True
        #     for k, v in base_dict.items():
        #         if k in w_dict and w_dict[k] >=v:
        #             pass
        #         else:
        #             competing = False
        #             break

        #     if competing and len(word) < min_l:
        #         min_l = len(word)
        #         res = word
        # return res