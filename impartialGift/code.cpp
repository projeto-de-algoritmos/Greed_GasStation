#include <algorithm>
#include<bits/stdc++.h>

using namespace std;
using ll = long long;

void solve(vector<ll> &a, vector<ll> &b, ll d){
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());

  ll i = a.size()-1, j = b.size() - 1;



  while (i >= 0 and j >= 0 ){

    if ( abs(a[i] - b[j]) <= d){
      cout << a[i] + b[j] << endl;;
      return;
    }

    if(b[j] > a[i]) j--; else i--;

  }


  cout << -1 << endl;
}

int main(){
  ll n, m, d;
  cin >> n >> m >> d;

  vector<ll> a(n), b(m);

  for ( auto &x : a)
    cin >> x;

  for ( auto &x : b)
    cin >> x;




  solve(a, b, d);


}
