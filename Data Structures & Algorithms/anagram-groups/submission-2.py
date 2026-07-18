class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        find = {}
        key = ""

        for i in range(len(strs)):
            chars = list(strs[i])
            chars.sort()
            key = ''.join(chars)
        
            if key not in find:
                find[key] = []
            find[key].append(strs[i])
        
        arr = list(find.values())
        return arr

