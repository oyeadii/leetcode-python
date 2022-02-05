class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(n):
            if (i+1)%3 ==0 and (i+1)%5==0:
                a.append("FizzBuzz")
            elif (i+1)%3 ==0:
                a.append("Fizz")
            elif (i+1)%5==0:
                a.append("Buzz")
            else:
                a.append(str(i+1))

        return a
