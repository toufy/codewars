// Human Readable Time
// https://www.codewars.com/kata/52685f7382004e774f0001f7
class HumanReadableTime {
    public static String makeReadable(int seconds) {
        int HH = seconds / 3600;
        int MM = (seconds % 3600) / 60;
        int SS = (seconds % 3600) % 60;
        return String.format("%02d:%02d:%02d", HH, MM, SS);
    }
}
