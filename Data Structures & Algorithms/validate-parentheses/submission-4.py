class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)<2):
            return False
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if (stack and s[i] == ')'):  
                if (stack.pop() != '('):
                    return False
            elif (stack and s[i] == ']'):  
                if (stack.pop() != '['):
                    return False
            elif (stack and s[i] == '}'):  
                if (stack.pop() != '{'):
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False