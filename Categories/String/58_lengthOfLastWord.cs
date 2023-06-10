public class Solution {
    public int LengthOfLastWord(string s) {
        string[] words = s.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int n = words.Length;
        
        return words[n - 1].Length;
    }
}