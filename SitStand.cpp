#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("sitin.txt","r",stdin);
    freopen("sitout.txt","w",stdout);
    int row,seat, tickets;
    cin>>row>>seat>>tickets;
    int nos= row*seat;
    if(tickets<=nos){
        cout<<tickets<<" "<<0<<" "<<endl;
    }else{
        cout<<nos<<" "<<(tickets-nos)<<endl;
    }
    }
