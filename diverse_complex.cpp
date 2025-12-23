// Poorly-styled code with bad practices
#include <iostream>
using namespace std;

// Global variables (bad practice)
int g_counter = 0;
int g_data[1000];

void processData() {
    for (int i = 0; i < 1000; i++) {
        if (i % 2 == 0) {
            g_data[i] = i * 2;
        } else if (i % 3 == 0) {
            g_data[i] = i + i;
        } else if (i % 5 == 0) {
            g_data[i] = i - 100;
        } else if (i % 7 == 0) {
            g_data[i] = i / 2;
        } else {
            g_data[i] = 0;
        }
        g_counter++;
    }
}

// Deeply nested if statements
void analyzeData() {
    for (int i = 0; i < 1000; i++) {
        if (g_data[i] > 0) {
            if (g_data[i] < 100) {
                if (g_data[i] % 2 == 0) {
                    if (g_data[i] % 3 == 0) {
                        cout << g_data[i] << endl;
                    }
                }
            }
        }
    }
}

int main() {
    processData();
    analyzeData();
    cout << "Counter: " << g_counter << endl;
    return 0;
}
