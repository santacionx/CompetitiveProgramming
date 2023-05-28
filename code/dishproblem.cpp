#include <bits/stdc++.h>
#include <limits.h>
using namespace std;
int main() {
    freopen("dishin.txt","r",stdin);
    freopen("dishout.txt","w",stdout);
    int n,sum=0,mini=INT_MAX;
    int maxi=INT_MIN;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum+=a[i];
    }
    for(int i=0;i<n;i++){
       if(a[i]<mini){
           mini=a[i];
       }

    }
     for(int i=0;i<n;i++){
       if(a[i]>maxi){
           maxi=a[i];
       }

    }
    cout<<mini<<" "<<maxi<<" "<<(sum/n)<<endl;
}
