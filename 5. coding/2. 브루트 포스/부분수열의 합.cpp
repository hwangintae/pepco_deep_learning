#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> arr(20);
int ans = 0;

int check(int n, int s, int count, int sum) {
	if (count == n) {
		if (sum == s) {
			ans++;
		}
		return ans;
	}
	check(n, s, count + 1, sum + arr[count]);
	check(n, s, count + 1, sum);
}

int main() {
	int n, s;
	int x;

	cin >> n >> s;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	check(n, s, 0, 0);

	if (s == 0) {
		ans--;
	}

	cout << ans << '\n';

	cin >> x;
}