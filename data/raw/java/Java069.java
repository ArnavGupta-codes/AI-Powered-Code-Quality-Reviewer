// Sample Java file Java069 for the ML code review dataset.

public class Java069 {
    public static long computeValue(int n) {
        long total = 0;
        for (int i = 0; i < n; i++) {
            total += (long) i * i;
        }
        return total;
    }

    public static void main(String[] args) {
        int n = 76;
        long result = computeValue(n);
        System.out.println("Result for Java069: " + result);
    }
}
