class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        n = len(strs)

        if n == 1:
            return [strs]
        
        freq_map = dict()

        for string in strs:
            # Get frequency array
            freq = [0] * 26
            for c in string:
                idx = ord(c) - ord('a')
                # print("Letter index: ", idx)
                freq[idx] += 1
            print("Frequency: ", freq)

            # Store string in map
            key = tuple(freq)
            print("Key: ", key)
            freq_map[key] = freq_map.get(key, []) + [string]

        print("Map: \n", freq_map)
        print("Map values: \n", freq_map.values())
        return list(freq_map.values())
    
                