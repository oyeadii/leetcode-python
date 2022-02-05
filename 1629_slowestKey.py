class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maximum  = 0
        for i in range(len(releaseTimes)):
            if i ==0:
                maximum = releaseTimes[0]
                j = i
            else:
                if maximum < (releaseTimes[i]- releaseTimes[i-1]):
                    maximum = releaseTimes[i]- releaseTimes[i-1]
                    j = i
                elif maximum == (releaseTimes[i]- releaseTimes[i-1]):
                    if ord(keysPressed[j]) > ord(keysPressed[i]):
                        j = j
                    else:
                        j = i
        return keysPressed[j]
