class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s1, s2, g1, g2 = '', '', '', ''
        for i in range(len(s)):
            if s[i] != goal[i]:
                if s1 == '':
                    s1, g1 = s[i], goal[i]
                elif s2 == '':
                    s2, g2 = s[i], goal[i]
                else:
                    return False
        if s1 == '':
            if len(set(s)) != len(s):
                return True
            else:
                return False
        return s1 == g2 and g1 == s2



def buddyStrings(A, B):
    if len(A) != len(B) or set(A) != set(B):
        return False

    # Check if A and B are equal
    if A == B:
        return len(set(A)) < len(A)  # Check if there are repeated characters in A

    # Find indices where characters differ
    indices = [i for i in range(len(A)) if A[i] != B[i]]

    # Check if there are exactly two differing indices
    return len(indices) == 2 and A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]

# Example usage:
A = "ab"
B = "ba"
result = buddyStrings(A, B)
print(result)  # Output: True
