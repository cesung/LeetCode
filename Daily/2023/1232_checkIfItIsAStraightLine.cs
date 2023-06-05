public class Solution {
    public bool CheckStraightLine(int[][] coordinates) {
        int n = coordinates.Length;
        if (n == 2) {
            return true;
        }

        int x0 = coordinates[0][0];
        bool is_vertical = true;
        for (int idx = 1; idx < n; idx++) {
            if (coordinates[idx][0] != x0) {
                is_vertical = false;
            }
        }
        if (is_vertical) {
            return true;
        }

        // exception: divide by 0 
        if (coordinates[1][0] - coordinates[0][0] == 0) {
            return false;
        }
        double slope = (
            (double)(coordinates[1][1] - coordinates[0][1]) /
            (coordinates[1][0] - coordinates[0][0])
        );

        double slope2;
        for (int idx = 2; idx < n; idx++) {

            // exception: divide by 0
            if (coordinates[idx][0] - coordinates[0][0] == 0) {
                return false;
            }
            slope2 = (
                (double)(coordinates[idx][1] - coordinates[0][1]) /
                (coordinates[idx][0] - coordinates[0][0])
            );


            if (slope != slope2) {
                return false;
            }
        }

        return true;
    }
}