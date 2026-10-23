class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, best = 0, 0
        mx_f = 0
        for r, ch in enumerate(s): # A
            count[ch] = count.get(ch, 0) + 1
            mx_f = max(mx_f, count[ch])
            if (r- l + 1) - mx_f > k:
                l += 1
            best = max(best, r - l + 1) 
        
        return best
        


