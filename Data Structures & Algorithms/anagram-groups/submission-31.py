class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_dict(s: str):
            d = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                d[idx] += 1
            return tuple(d)

        anagrams = defaultdict(list)
        for s in strs:
            anagrams[get_dict(s)].append(s)
        
        return list(anagrams.values())