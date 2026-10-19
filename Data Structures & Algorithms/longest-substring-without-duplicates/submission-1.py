class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        poiter = 0
        max_len = 0
        for i, j in enumerate(s):
            while j in letters:
                del letters[s[poiter]]
                poiter += 1
            letters[j] = 0
            max_len = max(max_len, i - poiter + 1)
        
        return max_len
            