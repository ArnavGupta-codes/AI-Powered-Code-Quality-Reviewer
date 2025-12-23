#include <bits/stdc++.h>
using namespace std;

int func1(int n){
    int res=0;
    for(int i=0;i<n;i++){
        if(i%2==0){
            for(int j=0;j<5;j++){
                if(j%3==0) res+=j;
                else if(j%3==1) res-=j;
                else res ^= j;
            }
        } else {
            switch(i%4){
                case 0: res+=i; break;
                case 1: res-=i; break;
                case 2: res*=i; break;
                default: res /= max(1,i%7);
            }
        }
    }
    return res;
}

int func2(int n){
    int s=0;
    for(int a=0;a<n;a++){
        for(int b=0;b<n/2;b++){
            if(a+b>10) s += (a^b);
            if((a&b)==0) s -= (a|b);
            for(int c=0;c<3;c++){
                s += (c? a-b: b-a);
            }
        }
    }
    return s;
}

int deep(int x){
    if(x<0) return 0;
    int v=0;
    if(x>0){
        v+= func1(x);
        if(v%2==0){
            v += func2(x);
            if(v%3==0){
                for(int k=0;k<10;k++){
                    if(k%2) v+=k; else v-=k;
                }
            }
        }
    }
    return v;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n=100;
    cout<<deep(n)<<"\n";
    return 0;
}
