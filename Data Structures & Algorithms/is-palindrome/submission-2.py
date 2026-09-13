class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        lowerS = s.lower()

        while left < right:
            if lowerS[left].isalnum() and lowerS[right].isalnum():
                if lowerS[left] != lowerS[right]:
                    return False
                right -= 1
                left += 1
            elif s[left].isalnum():
                right -=1
            elif s[right].isalnum():
                left +=1
            else:
                right -= 1
                left += 1
        return True
            
        