class Solution:
# This function simulates the process of pushing and popping elements onto and off the stack while iterating through the given pushed and popped sequences. If, at any point, the top element of the stack matches the current element in the popped sequence, it performs the pop operation

    # https://leetcode.com/problems/validate-stack-sequences/editorial/
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return i == len(popped)