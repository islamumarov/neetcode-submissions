class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = [0] * 26
        second = [0] * 26
        for c in s:
            first[ord(c) - ord("a")] += 1
        for t1 in t:
            second[ord(t1) - ord("a")] += 1
        for i in range(26):
            if first[i] != second[i]:
                return False

        return True
