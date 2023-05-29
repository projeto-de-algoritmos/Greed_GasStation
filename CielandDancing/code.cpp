#include <bits/stdc++.h>
	
using namespace std;

int main(){
	int n, m; 
	cin >> n >> m; //boy girl
	
	bitset<100> boy, girl;

	
	cout << n + m -1 << endl;

	for (int i = 1; i <= n; i++){
		for (int j =1; j <= m; j++ ){
			if (boy[i] == false || girl[j] == false){
					boy[i]= true; girl[j]=true;

					cout << i << " "<<j << endl;

			}
		}
	}



}

