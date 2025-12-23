// EXTREMELY BAD CODE - Multiple critical issues

#include <stdio.h>

int global_var1, global_var2, global_var3, global_var4, global_var5;
int g_array[10000];
static char* g_ptr = NULL;

void func1(int a) {
    if (a > 0) if (a > 1) if (a > 2) if (a > 3) if (a > 4) if (a > 5) if (a > 6) printf("nested\n");
}

void func2(int x, int y, int z, int w) {
    g_array[x*y*z*w] = 1;  // Buffer overflow!
}

void func3() {
    char buf[10];
    gets(buf);  // EXTREMELY UNSAFE
}

void func4() {
    int* p = malloc(10);
    p[100] = 5;  // Memory corruption
    // No free() - memory leak
}

void func5() {
    // TODO: Fix everything
    // TODO: Security issues
    // TODO: Memory leaks
    // TODO: Bad practices
    // FIXME: Rewrite this
    // FIXME: Dangerous code
    // FIXME: No documentation
    
    strcpy(g_ptr, "overflow");  // NULL pointer + buffer overflow
    sprintf(g_ptr, "%s%s%s%s", "a", "b", "c", "d");  // Format string
}

int main() {
    func1(10);
    func2(1000, 1000, 1000, 1000);
    func3();
    func4();
    func5();
    return 0;
}
