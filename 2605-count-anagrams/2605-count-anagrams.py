class Solution:
    def countAnagrams(self, s: str) -> int:
        # https://algo.monster/liteproblems/2514
        MOD = 10 ** 9 + 7
        # Pre-calculate factorial values modulo MOD
        factorials = [1]
        for i in range(1, 10**5 + 1):
            new_value = factorials[-1] * i % MOD
            factorials.append(new_value)        
        # Initialize the answer as 1
        answer = 1
      
        # Split the string into words
        for word in s.split():
            # Count the frequency of each character in the word
            character_counts = Counter(word)
            # Multiply the answer by the factorial of the length of the word
            answer *= factorials[len(word)]
            answer %= MOD
          
            # For each character, update the answer by multiplying with
            # the multiplicative inverse of the factorial of the character's count
            for count in character_counts.values():
                answer *= pow(factorials[count], -1, MOD)
                answer %= MOD
      
        return answer
