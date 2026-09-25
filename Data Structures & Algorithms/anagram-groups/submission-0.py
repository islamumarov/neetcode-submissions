class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            leters = [0] * 26
            for c in string:
                leters[ord('a') - ord(c)] +=1
            lstr = ','.join(str(i) for i in leters)
            if lstr not in groups:
                groups[lstr] = []
            groups[lstr].append(string)
        res = []
        for key,val in groups.items():
            res.append(val)
        
        return res

