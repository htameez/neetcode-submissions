class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if stack:
                if p == ')' and stack[-1] == '(':
                    stack.pop()
                elif p == '}' and stack[-1] == '{':
                    stack.pop()
                elif p == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        
        if stack:
            return False
        
        return True
