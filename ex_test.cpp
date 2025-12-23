/**
 *    author:  tourist
 *    created: 28.11.2025 09:43:54
**/
#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int tt;
  cin >> tt;
  while (tt--) {
    int n, q;
    cin >> n >> q;
    string s;
    cin >> s;
    int val = 0;
    int ranges = 0;
    int qs = 0;
    for (int i = 0; i < n; i++) {
      val += (s[i] == 'X' ? 10 : (s[i] == 'V' ? 5 : (s[i] == 'I' ? 1 : 0)));
      ranges += int(s[i] == 'I' && i < n - 1 && s[i + 1] != 'I');
      qs += (s[i] == '?' ? 1 : 0);
    }
    vector<int> delta(n);
    set<pair<int, int>> st;
    for (int i = 0; i < n; i++) {
      if (s[i] == '?') {
        delta[i] = +1;
        if (i > 0 && s[i - 1] == 'I') {
          delta[i] -= 1;
        }
        if (i == n - 1 || s[i + 1] == 'I') {
          delta[i] -= 1;
        }
        st.emplace(delta[i], i);
      }
    }
    vector<int> rs = {ranges};
    while (!st.empty()) {
      auto it = prev(st.end());
      int i = it->second;
      st.erase(it);
      ranges += delta[i];
      rs.push_back(ranges);
      for (int j = i - 1; j <= i + 1; j += 2) {
        if (j >= 0 && j < n && s[j] == '?') {
          if (st.find({delta[j], j}) != st.end()) {
            st.erase({delta[j], j});
            delta[j] -= 1;
            st.emplace(delta[j], j);
          }
        }
      }
    }
    assert(int(rs.size()) == qs + 1);
    while (q--) {
      int cx, cv, ci;
      cin >> cx >> cv >> ci;
      int take_i = min(ci, qs);
      int take_v = min(cv, qs - take_i);
      int take_x = qs - take_i - take_v;
      int ans = val + take_i * 1 - 2 * rs[take_i] + take_v * 5 + take_x * 10;
      cout << ans << '\n';
    }
  }
  return 0;
}
