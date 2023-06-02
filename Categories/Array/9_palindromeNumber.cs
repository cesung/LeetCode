public class Solution {
    private List<int> GetDigits(int x) {
        var ret = new List<int>();
        while (x > 0) {
            ret.Add(x % 10);
            x /= 10;
        }

        return ret;
    }
    public bool IsPalindrome(int x) {
        if (x < 0) return false;
        var digits = GetDigits(x);
        int digitsLength = digits.Count;

        int idx = 0, jdx = digitsLength - 1;
        while (idx < jdx) {
            if (digits[idx] != digits[jdx]) return false;            
            idx++;
            jdx--;
        }
        
        return true;
    }
}