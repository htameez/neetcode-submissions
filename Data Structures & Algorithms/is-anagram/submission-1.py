class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make dictionary (hash table) for each string with character counts
        # loop through each and check if character counts equal
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        chars1 = {}
        chars2 = {}

        for char1 in s_sorted:
            if char1 in chars1:
                chars1[char1] = chars1[char1] + 1+ 1
            else:
                chars1[char1] = 1
        
        for char2 in t_sorted:
            if char2 in chars2:
                chars2[char2] = chars2[char2] + 1+ 1
            else:
                chars2[char2] = 1

        if chars1 == chars2:
            return True
        return False
        
