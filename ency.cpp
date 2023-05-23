#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("encyin.txt","r",stdin);
    freopen("encyout.txt","w",stdout);
    int n,q,pno;
    cin>>n>>q;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<q;i++){
        cin>>pno;
        cout<<a[pno-1]<<endl;

    }
}
