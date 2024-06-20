from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:        
        def shift_letter(letter: str, shift: int):
            return chr((ord(letter) - shift) % 26 + ord('a'))
        
        # Create a hash value
        def get_hash(string: str):
            # Calculate the number of shifts to make the first character to be 'a'
            shift = ord(string[0])
            return ''.join(shift_letter(letter, shift) for letter in string)
        
        # Create a hash_value (hashKey) for each string and append the string
        # to the list of hash values i.e. mapHashToList["abc"] = ["abc", "bcd"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)
        
        # Return a list of all of the grouped strings
        return list(groups.values())

        # def get_hash(s):
        #     if len(s) == 1:
        #         return '1'
        #     key = ''
        #     for i in range(1, len(s)):
        #         diff = ord(s[i]) - ord(s[i-1])
        #         if diff < 0:
        #             diff = diff + 26
        #         key += str(diff) + '_'
        #     return key

        # ans = []
        # hm = defaultdict(list)
        # for s in strings:
        #     key = get_hash(s)
        #     hm[key].append(s)
       
        # ans = [list(hm[s]) for s in hm]
       
        # return ans