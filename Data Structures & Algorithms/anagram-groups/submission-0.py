class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make one hash map with all strings; map strings to array with character and counts

        groups = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
        