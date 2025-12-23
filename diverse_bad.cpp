#include<bits/stdc++.h>
using namespace std;
int main(){int*arr=new int[100];for(int i=0;i<100;i++)arr[i]=i;int s=0;for(int i=0;i<100;i++){if(i%2==0){s+=arr[i];}else if(i%3==0){s-=arr[i];}else if(i%5==0){s*=2;}}cout<<s;delete[]arr;return 0;}
