// Sample C++ file cpp049 for the ML code review dataset.

#include <bits/stdc++.h>
using namespace std;

long long compute_value(int n) {
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += 1LL * i * i;
    }
    return total;
}

int main() {
    int n = 54;
    cout << "Result for cpp049: " << compute_value(n) << "\n";
    return 0;
}
