class Solution:
    def isValid(self, s: str) -> bool:
        def match(a,b):
            if a=='(' and b==')':
                return True
            elif a=='{' and b=='}':
                return True
            elif a=='[' and b==']':
                return True
            else:
                return False
        s = list(s)
        stack = []
        open = ['(', '{', '[']
        close = [')', '}', ']']
        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            elif s[i] in close:
                if len(stack)==0:
                    return False
                elif match(stack[len(stack)-1],s[i]) == True:
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True
                
