public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        int minLength = strs.Min(str => str.Length);
        int commonUntil = -1;
        bool isCommon = true;
        
        for (int idx = 0; idx < minLength; idx++) {
            char target = strs[0][idx];
            foreach (string str in strs) {
                if (str[idx] != target) {
                    isCommon = false;
                    break;
                }
            }
            if (!isCommon) {
                break;
            }
            commonUntil = idx;
        }

        return strs[0].Substring(0, commonUntil + 1);
    }
}