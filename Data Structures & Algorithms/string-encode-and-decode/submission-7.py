class Solution:

    def encode(self, strs: List[str]) -> str:
        # loop thru each string and concatenate to another string
        encodedStr = ""

        for i in range(len(strs) - 1):
            encodedStr += strs[i] + "❤️"
        
        if strs:
            encodedStr += strs[len(strs) - 1]
        
        if not strs:
            return "❤️"
        return encodedStr

    def decode(self, s: str) -> List[str]:
        # parse thru input string by spaces and divide into strings
        result = s.split("❤️")
        if s == "❤️":
            return []
        else:
            if s == "":
                return [""]
        return result