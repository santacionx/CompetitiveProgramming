#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("tripin.txt","r",stdin);
    freopen("tripout.txt","w",stdout);
    int n;
    cin>>n;
    int a[n],count=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        if(a[i]%3==0){
            count++;
        }
    }
    if(count==0){
        cout<<"Nothing here!"<<endl;
    }else{
        cout<<count<<endl;
        for(int i=0;i<n;i++){
            if(a[i]%3==0){
                cout<<i+1<<" ";
            }
        }
    }

}
