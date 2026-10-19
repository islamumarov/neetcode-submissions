class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def get(s):
            longest = 0
            letters = {}
            pointer = 0
            for i, j in enumerate(s):
                letters[j] = letters.get(j, 0) + 1
                while i - pointer - letters[s[pointer]] + 1 > k:
                    letters[s[pointer]] -= 1
                    if letters[s[pointer]] == 0:
                        del letters[s[pointer]]
                    pointer += 1
                longest = max(longest, i - pointer + 1)
            return longest

        return max(get(s), get(s[::-1]))
