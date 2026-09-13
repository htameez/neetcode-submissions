class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        letters2 = {}

        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        
        for char in t:
            if char in letters2:
                letters2[char] += 1
            else:
                letters2[char] = 1
        
        if letters == letters2:
            return True
        return False

