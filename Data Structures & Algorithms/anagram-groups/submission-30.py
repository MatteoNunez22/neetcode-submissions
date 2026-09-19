class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            fArray = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                fArray[i] += 1
            anagrams[tuple(fArray)].append(word)
        
        return list(anagrams.values())