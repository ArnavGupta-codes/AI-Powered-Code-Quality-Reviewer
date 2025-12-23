// ABSOLUTE WORST CODE POSSIBLE - Complete anti-patterns
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int g1, g2, g3, g4, g5, g6, g7, g8, g9, g10;
int* gp1; int* gp2; int* gp3;
static char gb[100];

void a(int x) {
    if(x>0)if(x>1)if(x>2)if(x>3)if(x>4)if(x>5)if(x>6)if(x>7)if(x>8)printf("x");
}

void b() {
    char buf[5]; gets(buf); strcpy(gb, buf); // Multiple buffer overflows
}

void c(int* p) {
    int* q = malloc(10);
    q[100] = *p; // Buffer overflow and potential null deref
}

void d() {
    // TODO
    // FIXME
    // TODO
    // FIXME
    // TODO
    strcpy(gp1, "test"); // Null pointer + overflow
    sprintf(gp2, "%s%s%s%s%s", "a", "b", "c", "d", "e"); // Format string
}

int e(int a, int b, int c, int d, int e, int f) {
    if(a)if(b)if(c)if(d)if(e)if(f)return a+b+c+d+e+f;
}

int main() {
    int x[10]; x[1000]=5; // OOB
    a(5); b(); int* p=0; c(p); d(); e(1,2,3,4,5,6);
    return 0;
}
