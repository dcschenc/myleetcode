class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

        ans = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            ones = 0
            if i >= 0 and a[i] == '1':
                ones += 1 
            if j >= 0 and b[j] == '1':
                ones += 1 
            if carry == 1:
                ones += 1 
            
            if ones == 0:
                ans = ans + "0"
            elif ones == 1:
                ans = ans + '1'
                carry = 0
            elif ones == 2:
                ans = ans + '0'
                carry = 1
            else:
                ans = ans + '1'
                carry = 1

            i -= 1 
            j -= 1 
        return ans[::-1]        