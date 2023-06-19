// Find the Parity Outlier
// https://www.codewars.com/kata/5526fc09a1bbd946250002dc
class FindOutlier {
    static int find(int[] integers) {
        int countEven = 0, countOdd = 0;
        for (int i = 0; i < 3; i++) {
            if (integers[i] % 2 == 0) {
                countEven++;
            } else {
                countOdd++;
            }
        }
        if (countEven > countOdd) {
            for (int j = 0; j < integers.length; j++) {
                if ((integers[j] & 1) == 1) {
                    return integers[j];
                }
            }
        } else {
            for (int j = 0; j < integers.length; j++) {
                if ((integers[j] & 1) == 0) {
                    return integers[j];
                }
            }
        }
        return 0;
    }
}
