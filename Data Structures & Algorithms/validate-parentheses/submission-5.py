class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        for c in s:
            if paren:
                if c == ')' and paren[-1] == '(':
                    paren.pop()
                    continue
                elif c == '}' and paren[-1] == '{':
                    paren.pop()
                    continue
                elif c == ']' and paren[-1] == '[':
                    paren.pop()
                    continue
            paren.append(c)
        if not paren:
            return True
        else:
            return False