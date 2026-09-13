class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            charCount = [0] * 26
            for ch in s:
                charCount[ord(ch) - ord('a')] += 1
            
            key = tuple(charCount)

            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)
        
        return list(groups.values())
        