class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Edge case
        if len(strs) == 1: return [strs]
        
        freq_map = dict()   # Annagram hashmap
        for string in strs: # O(n)
            # Get frequency array
            freq_array = [0] * 26 # Initiate frequency array
            for c in string:    # O(m)
                idx = ord(c) - ord('a') # Get character codes for index
                freq_array[idx] += 1    # Update frequency

            # Store string in map
            key = tuple(freq_array) # Convert array to key
            freq_map[key] = freq_map.get(key, []) + [string]    # Add annagram

        return list(freq_map.values())  # Return lists of annagrams

        # Time: O(n + m), Space: O(n)
                