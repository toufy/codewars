// Array.diff
// https://www.codewars.com/kata/523f5d21c841566fde000009

import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

class Kata {
    public static int[] arrayDiff(int[] a, int[] b) {
        ArrayList<Integer> aNew = Arrays.stream(a).boxed().collect(Collectors.toCollection(ArrayList::new));
        for (int i = 0; i < b.length; i++) {
            int diff = b[i];
            while (aNew.contains(diff)) {
                aNew.remove(Integer.valueOf(diff));
            }
        }
        return aNew.stream().mapToInt(k -> k).toArray();
    }
}
