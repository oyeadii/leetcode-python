class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if 65<= ord(word[0]) <91:
            if 65<= ord(word[1]) <91:
                for i in range(2,len(word)):
                    if 65<= ord(word[i]) <91:
                        continue
                    else: 
                        return False
                return True
            else:
                for i in range(2,len(word)):
                    if 97<= ord(word[i]) <123:
                        continue
                    else: 
                        return False
                return True
        else:
            for i in range(1, len(word)):
                if 97<= ord(word[i]) <123:
                        continue
                else: 
                    return False
            return True
