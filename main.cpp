#include <bits/stdc++.h>
using namespace std;

int main()
{
    for(int i=0;;i++)
    {
        int sum=0;
        int length=0;        
        
        int a=i,b=i;      
        for(length=0;b>0;length++, b /= 10){}
        for(sum=0;a>0;sum += pow((a % 10),length), a /= 10){}
        if(sum == i){
            cout<<i<<endl;
        }
    }
    return 0;
}