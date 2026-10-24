class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        need, win = [0] * 26, [0] * 26
        for c in s1:
            need[ord(c) - 97] += 1

        l = 0
        for i, c in enumerate(s2):
            win[ord(c) - 97] += 1                 # add right
            if i-k > l-1 :
                win[ord(s2[i - k]) - 97] -= 1     # drop left
            if win == need:                       # compare 26 ints
                return True
        return False