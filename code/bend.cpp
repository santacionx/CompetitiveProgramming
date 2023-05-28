#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("bendin.txt","r",stdin);
    freopen("bendout.txt","w",stdout);
    int x1,x2,x3,x4,y1,y2,y3,y4;
    cin>>x1>>y1>>x2>>y2>>x3>>y3>>x4>>y4;
    int area1=(x2-x1)*(y2-y1);
    int area2=(x4-x3)*(y4-y3);
    int areaIntersection=0;
    int leftintersection=max(x1,x3);
    int rightintersection=min(x2,x4);
    int bottomintersection=max(y1,y3);
    int topintersection=min(y2,y4);
    if((leftintersection<rightintersection)&& (bottomintersection<topintersection)){
        areaIntersection=(leftintersection-rightintersection)*(bottomintersection-topintersection);
    }
    int ans=area1+area2-areaIntersection;
    cout<<ans<<endl;
    return 0;
}