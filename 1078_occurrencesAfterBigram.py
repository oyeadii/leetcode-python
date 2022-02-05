class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        a = []
        text = text.split(' ')

        for i in range(len(text)-2):
            if text[i] == first:
                if text[i+1]==second:
                    a.append(text[i+2])

        return a
