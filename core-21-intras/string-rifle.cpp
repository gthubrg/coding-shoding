#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string unique(string s)
{
    string st;
    int len = s.length();
    for(int i = 0; i < len; i++)
    {
        char a=s[i];
        auto f = st.find(a);
        if (f==std::string::npos)
        {
            st+=a;
        }
    }
    return st;
}
int main() {
    int a;
    cin >> a;
    while(a--)
    {
        string s;
        cin >> s;
        cout  << unique(s) << endl;
    }
}
