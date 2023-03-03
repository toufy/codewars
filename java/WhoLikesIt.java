class Solution {
    public static String whoLikesIt(String... names) {
        switch (names.length) {
            case 0:
                return "no one likes this";
            case 1:
                return names[0] + " likes this";
            case 2:
                return String.format("%1$s and %2$s like this",
                                        names[0], names[1]);
            case 3:
                return String.format("%1$s, %2$s and %3$s like this",
                                        names[0], names[1], names[2]);
            default:
                return String.format("%1$s, %2$s and %3$d others like this",
                                        names[0], names[1], names.length-2);
        }
    }
}
