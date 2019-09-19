#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int cal(vector<int> &v) {
	int sum = 0;
	for (int i = 1; i < v.size(); i++) {
		sum += abs(v[i] - v[i-1]);
	}
	return sum;
}

int main() {
	int num;
	int i;
	int max = 0;
	int ans = 0;
	cin >> num;

	vector<int> arr(num);

	for (i = 0; i < num; i++) {
		cin >> arr[i];
	}

	sort(arr.begin(), arr.end());

	do {
		ans = cal(arr);
		max = max > ans ? max : ans;
	} while(next_permutation(arr.begin(), arr.end()));

	cout << max << '\n';
}