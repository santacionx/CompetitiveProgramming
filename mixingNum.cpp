#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("mixin.txt","r",stdin);
    freopen("mixout.txt","w",stdout);
    int n,d,div,rem;
    cin>>n>>d;
    div=n/d;
    rem=n%d;
    if(rem==0){
        cout<<div<<endl;
    }else{
        cout<<div<<" "<<rem<<"/"<<d<<endl;
    }
}
