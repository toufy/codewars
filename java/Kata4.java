// Sort the odd
// https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

import java.util.PriorityQueue;

class Kata {
    public static int[] sortArray(int[] array) {
        PriorityQueue<Integer> indecies = new PriorityQueue<Integer>();
        PriorityQueue<Integer> odds = new PriorityQueue<Integer>();
        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 != 0) {
                odds.add(array[i]);
                indecies.add(i);
            }
        }
        while (!odds.isEmpty()) {
            int index = indecies.poll();
            int odd = odds.poll();
            array[index] = odd;
        }
        return array;
    }
}
