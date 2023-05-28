#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("taktakin.txt","r",stdin);
    freopen("taktakout.txt","w",stdout);
    int friuits,count=0;
    cin>>friuits;
    while((friuits%11 )!=1){
        friuits*=2;
        count++;

    }
    cout<<count<<" "<<friuits<<endl;

}