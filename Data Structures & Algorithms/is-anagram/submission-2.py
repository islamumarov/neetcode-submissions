class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [0] * 26
        t_arr =  [0] * 26
        for c in s:
            s_arr[ord('a') - ord(c)] +=1
        for c in t:
            t_arr[ord('a') - ord(c)] +=1
        
        for i in range(26):
            if s_arr[i] != t_arr[i]:
                return False
        
        return True

