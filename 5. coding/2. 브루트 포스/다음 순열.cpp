#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int num;
	vector<int> v;
	cin >> num;

	for (int i = 0; i < num; i++) {
		cin >> v[i];
	}
	if (next_permutation(v.begin(), v.end())) {
		for (int i = 0; i < num; i++) {
			cout << v[i] << " ";
		}
	}
	else {
		cout << "-1";
	}
	cout << '\n';
}