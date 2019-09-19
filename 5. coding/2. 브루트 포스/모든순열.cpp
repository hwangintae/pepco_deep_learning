#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int num, x;
	cin >> num;
	vector<int> v(num);

	for (int i = 1; i <= num; i++) {
		v[i-1] = i;
	}

	for (int i = 0; i < num; i++) {
		cout << v[i] << ' ';
	}
	cout << '\n';
	while(next_permutation(v.begin(), v.end())) {
		for (int i = 0; i < num; i++) {
			cout << v[i] << ' ';
		}
		cout << '\n';
	}
	cin >> x;
}