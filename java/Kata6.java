// Build Tower
// https://www.codewars.com/kata/576757b1df89ecf5bd00073b
class Kata {
    public static String[] towerBuilder(int nFloors) {
        String[] floors = new String[nFloors];
        int base = ((nFloors - 1) * 2) + 1;
        for (int i = 0; i < nFloors; i++) {
            int blocks = 1 + (2 * i);
            int spaces = (base - blocks) / 2;
            String floor = String.valueOf(' ').repeat(spaces) + String.valueOf('*').repeat(blocks)
                    + String.valueOf(' ').repeat(spaces);
            floors[i] = floor;
        }
        return floors;
    }
}
