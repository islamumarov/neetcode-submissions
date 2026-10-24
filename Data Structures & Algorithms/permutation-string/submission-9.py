class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        letter_s1 = [0] * 26
        letter_s2 = [0] * 26
        for i, j in enumerate(s1):
            letter_s1[ord(j) - ord('a')] +=1
            letter_s2[ord(s2[i]) - ord('a')] +=1
        
        match = 0
        need = 0
        for i in range(26):
            if letter_s1[i] != letter_s2[i]:
                need +=1
        if need == 0: return True
        l = 0
        for i in range(len(s1), len(s2)): # need=2, 3
            idx = ord(s2[i]) - ord('a')
            if letter_s2[idx] == letter_s1[idx]:
                need +=1
            
            letter_s2[idx] +=1
            while (i - len(s1)) == l:
                l_idx = ord(s2[l]) - ord('a')
                if letter_s2[l_idx] == letter_s1[l_idx]:
                    need +=1
                letter_s2[l_idx] -= 1
                if letter_s2[l_idx] == letter_s1[l_idx]: need -=1
                l +=1
            if letter_s2[idx] == letter_s1[idx]: need -=1
            if need == 0:
                return True
        
        return False
        



