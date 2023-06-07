public class Solution {
    public int MinFlips(int a, int b, int c) {
        int cnt = 0;
        int a_bit, b_bit, c_bit;
        while (
            a > 0 ||
            b > 0 ||
            c > 0
        ) 
        {
            a_bit = a % 2;
            b_bit = b % 2;
            c_bit = c % 2;
            
            if (c_bit == 0) {
                cnt += (a_bit + b_bit);
            }
            else {
                cnt = (
                    a_bit == 0 && 
                    b_bit == 0
                ) ? cnt + 1 : cnt;
            }

            a /= 2;
            b /= 2;
            c /= 2;
        }

        return cnt;
    }
}