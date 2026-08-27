class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Compare character by character across all strings
            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
                    
        return strs[0]
        