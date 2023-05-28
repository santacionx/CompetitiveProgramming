#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("rainin.txt","r",stdin);
    freopen("rainout.txt","w",stdout);
    int n,tank,sum=0;
    cin>>n>>tank;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n;){
        sum+=a[i];
       if(sum==tank){
           cout<<i+1<<endl;
          break;
       }else if(sum >tank){
           cout<<i+1<<endl;
           break;
       }else{
           i++;
       }

    }
  
}
