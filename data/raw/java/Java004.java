// Sample Java file Java004 for the ML code review dataset.

public class Java004 {
    public static long computeValue(int n) {
        long total = 0;
        for (int i = 0; i < n; i++) {
            total += (long) i * i;
        }
        return total;
    }

    public static void main(String[] args) {
        int n = 11;
        long result = computeValue(n);
        System.out.println("Result for Java004: " + result);
    }
}
