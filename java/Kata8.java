// Data Reverse
// https://www.codewars.com/kata/569d488d61b812a0f7000015

import java.util.Stack;

class Kata {
    public static int[] DataReverse(int[] data) {
        int[] reversedBits = new int[data.length];
        int segments = data.length / 8;
        int currBit = 0, revBit = 0;
        Stack<int[]> streamStack = new Stack<>();

        for (int aSegment = 0; aSegment < segments; aSegment++) {
            int[] bitArray = new int[8];
            for (int i = 0; i < 8; i++) {
                bitArray[i] = data[currBit];
                currBit++;
            }
            streamStack.add(bitArray);
        }

        while (!streamStack.isEmpty()) {
            int[] bitArray = streamStack.pop();
            for (int aBit = 0; aBit < bitArray.length; aBit++) {
                reversedBits[revBit] = bitArray[aBit];
                revBit++;
            }
        }

        return reversedBits;
    }
}
