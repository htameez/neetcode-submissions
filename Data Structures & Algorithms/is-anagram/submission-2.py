class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        s_hash = {}
        t_hash = {}

        for c in s_sorted:
            if c in s_hash:
                s_hash[c] += 1
            else:
                s_hash[c] = 1
        
        for c in t_sorted:
            if c in t_hash:
                t_hash[c] += 1
            else:
                t_hash[c] = 1
                
        if s_hash == t_hash:
            return True

        return False