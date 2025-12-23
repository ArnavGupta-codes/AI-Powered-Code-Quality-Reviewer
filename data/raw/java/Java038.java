// Sample Java file Java038 for the ML code review dataset.

public class Java038 {
    public static long computeValue(int n) {
        long total = 0;
        for (int i = 0; i < n; i++) {
            total += (long) i * i;
        }
        return total;
    }

    public static void main(String[] args) {
        int n = 45;
        long result = computeValue(n);
        System.out.println("Result for Java038: " + result);
    }
}
