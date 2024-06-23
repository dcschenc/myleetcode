class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(0, n):
            j = i + 1
            divisibleBy3 = j%3 == 0
            divisibleBy5 = j%5 == 0
            result = ""
            if divisibleBy3:
                result = 'Fizz'
            if divisibleBy5:
                result += 'Buzz'
            if result == "":
                result = str(j)
            answer.append(result)
            # if j%3 == 0 and j%5 == 0:
            #     answer.append('FizzBuzz')
            # elif j%3 == 0:
            #     answer.append('Fizz')
            # elif j%5 == 0:
            #     answer.append('Buzz')
            # else:
            #     answer.append(str(j))
        return answer
