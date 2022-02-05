class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        i=0
        while True:
            if ransomNote[i] in magazine:
                magazine.remove(ransomNote[i])
                if i+1 == len(ransomNote):
                    return True
                    break
                i+=1
            else:
                return False
                break
