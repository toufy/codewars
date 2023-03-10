class PangramChecker {
    public boolean check(String sentence){
        sentence = sentence.toLowerCase();
        String alphabet = "abcdefghigklmnopqrstuvwxyz";
        for (int i = 0; i < alphabet.length(); i++) {
            if (!(sentence.contains(Character.toString(alphabet.charAt(i))))) {
                return false;
            }
        }
        return true;
    }
}
