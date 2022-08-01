#include <bits/stdc++.h>

using namespace std;

void selectionSort(vector<int> &v) {
    int n=v.size(),min_index;
    for(int i=0;i<n-1;i++) {
        min_index=i;
        for(int j=i+1;j<n;j++) {
            if(v[min_index]>v[j])
                min_index=j;
        }
        int temp=v[min_index];
        v[min_index]=v[i];
        v[i]=temp;
    }
}

int main()
{
    vector<int> v={3,4,1,2,8,9,0,5};
    selectionSort(v);
    for(auto x : v)
        cout<<x<<" ";
    return 0;
}
