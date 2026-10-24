class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter()
        need = len(s1_count)
        have = 0

        l = 0
        for i, j in enumerate(s2):
            while i - l > len(s1)-1:
                s2_count[s2[l]] -= 1
                if s2[l] in s1_count and s2_count[s2[l]] < s1_count[s2[l]]:
                    have -=1
                l +=1
            
            s2_count[j] += 1
            if j in s1_count and s2_count[j] == s1_count[j]:
                have +=1
            if have == need:
                return True
            
        
        return False


#Input: s1 = "abc", s2 = "lecaabee"
#                           | 

