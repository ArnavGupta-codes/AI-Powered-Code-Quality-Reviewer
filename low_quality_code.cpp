#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Bad global variables
int g_count = 0;
int g_data[1000];
char g_buffer[256];

// Function with poor practices
void doSomething(int a, int b, int c, int d, int e) {
    if (a > 0) {
        if (b > 0) {
            if (c > 0) {
                if (d > 0) {
                    if (e > 0) {
                        printf("Value: %d\n", a + b + c + d + e);
                    }
                }
            }
        }
    }
}

// Unsafe function with buffer overflow risk
void copyString(char* dest, char* src) {
    strcpy(dest, src);  // DANGEROUS!
}

// Function with unclear logic
int calc(int x) {
    int y = x * 2;
    int z = y + x;
    int w = z - 5;
    int q = w * w;
    int r = q / 2;
    return r;
}

// Main with no error handling
int main() {
    int arr[10];
    int i;
    
    // Loop without clear purpose
    for (i = 0; i < 100; i++) {
        arr[i] = i * 2;  // Out of bounds!
        g_data[i] = i;
        g_count++;
    }
    
    // TODO: Fix this code
    // FIXME: This is broken
    
    doSomething(1, 2, 3, 4, 5);
    calc(10);
    
    char name[50];
    copyString(name, "This is a very long string that will overflow the buffer");
    
    printf("%s\n", name);
    
    return 0;
}
