class Solution {
    public boolean isAnagram(String s, String t) {
        int sizeS = s.length();
        int sizeT = t.length();
        if (sizeS != sizeT) {
            return false;
        }

        HashMap<Character, Integer> dictS = new HashMap<>();
        HashMap<Character, Integer> dictT = new HashMap<>();

        for (int i = 0; i < sizeS; i++) {
            dictS.put(s.charAt(i), dictS.getOrDefault(s.charAt(i), 0) + 1);
            dictT.put(t.charAt(i), dictT.getOrDefault(t.charAt(i), 0) + 1);
        }

        return dictS.equals(dictT);
    }
}
