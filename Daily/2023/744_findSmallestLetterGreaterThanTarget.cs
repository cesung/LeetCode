public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        int n = letters.Length;
        int left = 0, right = n - 1;

        while (left < right) 
        {
            int mid = (left + right) / 2;
            if ( (int)letters[mid] <= (int)target ) 
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }

        return (int)letters[left] <= (int)target ? letters[0] : letters[left];
    }
}