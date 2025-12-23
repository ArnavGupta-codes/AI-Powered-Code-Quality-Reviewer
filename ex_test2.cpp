#include <bits/stdc++.h>
using namespace std;

#define int long long
const int M = 998244353;
#define all(x) x.begin(), x.end()
#define edl "\n"
#define pb push_back
#define inf INT_maxx
#define YES() cout << "YES\n"
#define NO() cout << "NO\n"
#define HEHE() cout << "HEHE\n"
#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) a*b/__gcd(a,b)
#define input(a) for (int i = 0; i < (int)a.size(); i++) cin >> a[i]
#define vout(a) for (auto x : a) { cout << x << " "; } cout << "\n"
#define precise(x, y) cout << fixed << setprecision(y) << x
bool perfectSqr(int n) { return floor(sqrt(n)) == ceil(sqrt(n)); }

void dfs(int cur, int par, vector<int>& v, vector<vector<int>>& g, vector<int>& maxx, vector<int>& minn){
    if(par != -1){
        maxx[cur] = max(v[cur]-minn[par],v[cur]);
        minn[cur] = v[cur]-maxx[par];
    }
    for (auto it: g[cur])
    {
        if(it != par){
            dfs(it,cur,v,g,maxx,minn);
        }
    }
    
}

void solve() {
    int n;
    cin >> n;
    vector<int> v(n);
    input(v);
    vector<vector<int>> g(n);
    for (int i = 0; i < n-1; i++)
    {
        int x, y;
        cin >> x >> y;
        g[x-1].pb(y-1);
        g[y-1].pb(x-1);
    }
    
    vector<int> maxx(n,0);
    vector<int> minn(n,0);
    maxx[0] = v[0];
    minn[0] = v[0];
    dfs(0,-1,v,g,maxx,minn);

    vout(maxx);
    
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
}