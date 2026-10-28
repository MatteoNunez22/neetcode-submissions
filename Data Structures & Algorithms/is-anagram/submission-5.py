class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            c_s, c_t = s[i], t[i]
            dict_s[c_s] = dict_s.get(c_s, 0) + 1
            dict_t[c_t] = dict_t.get(c_t, 0) + 1

        return dict_s == dict_t
                     