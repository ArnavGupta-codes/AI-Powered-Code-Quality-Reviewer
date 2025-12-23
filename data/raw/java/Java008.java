// Sample Java file Java008 for the ML code review dataset.

public class Java008 {
    public static long computeValue(int n) {
        long total = 0;
        for (int i = 0; i < n; i++) {
            total += (long) i * i;
        }
        return total;
    }

    public static void main(String[] args) {
        int n = 15;
        long result = computeValue(n);
        System.out.println("Result for Java008: " + result);
    }
}
