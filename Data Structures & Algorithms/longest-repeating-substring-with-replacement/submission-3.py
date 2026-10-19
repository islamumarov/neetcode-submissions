class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, best = 0, 0
        mx_f = 0
        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            mx_f = max(mx_f, count[ch])
            while (r- l + 1) - mx_f > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        
        return best
