// TERRIBLE JAVA CODE
public class WorstCode {
    public static int g1, g2, g3, g4, g5;
    public static String[] gs;
    
    public static void a(int x) {
        if(x>0)if(x>1)if(x>2)if(x>3)if(x>4)if(x>5)System.out.println("x");
    }
    
    public static void b(String s) {
        // TODO fix this
        // FIXME broken
        // TODO needs work
        // FIXME security issue
        Object obj = null;
        System.out.println(obj.toString());  // Null pointer
    }
    
    public static void c() {
        try {
            int[] arr = new int[5];
            arr[1000] = 5;  // ArrayIndexOutOfBounds
        } catch(Exception e) {
            // Silent failure - bad practice
        }
    }
    
    public static int d(int a,int b,int c,int d,int e,int f,int g) {
        if(a>0)if(b>0)if(c>0)if(d>0)if(e>0)if(f>0)if(g>0)return a+b+c+d+e+f+g;
        return 0;
    }
    
    public static void main(String[] args) {
        a(5);
        b("test");
        c();
        d(1,2,3,4,5,6,7);
    }
}
