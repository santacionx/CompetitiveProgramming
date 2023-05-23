#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("listin.txt","r",stdin);
    freopen("listout.txt","w",stdout);
    int n;
    cin>>n;
    int a[1001];
    for(int i=0;i<1001;i++){
        a[i]=0;
    }
    for(int i=0;i<n;i++){
        int p1,p2;
        cin>>p1>>p2;
        a[p1]++;
        a[p2]++;
    }
   int max=0;
   for(int i=0;i<1001;i++){
       if(a[i]>max){
           max=a[i];
       }
   }
   for(int i=0;i<1001;i++){
       if(a[i]==max){
           cout<<i<<endl;
       }
   }
    }


