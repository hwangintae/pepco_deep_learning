#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int check(int l, vector<char> &ans) {
	int mo = 0, ja = 0;
	for (int i = 0; i < l; i++) {
		if (ans[i] == 'a' || ans[i] == 'e' || ans[i] == 'i' || ans[i] == 'o' || ans[i] == 'u')
			mo++;
		else
			ja++;
	}
	if (mo >= 1 && ja >= 2) {
		sort(ans.begin(), ans.end());
		for (int i = 0; i < l; i++) {
			cout << ans[i];
		}
		cout << '\n';
	}
	return 0;
}

int make_pw(int l, vector<char> &arr) {
	vector<int> choose(l, 0);
	
	for (int i = 0; i < arr.size() - l; i++) {
		choose.push_back(1);
	}
	do {
		vector<char> ans;
		for (int i = 0; i < arr.size(); i++) {
			if (choose[i] == 0) {
				ans.push_back(arr[i]);
			}
		}
		check(l, ans);
	} while (next_permutation(choose.begin(), choose.end()));
	return 0;
}

int main() {
	int l, c;
	cin >> l >> c;

	vector<char> arr(c);
	for (int i = 0; i < c; i++) {
		cin >> arr[i];
	}

	sort(arr.begin(), arr.end());

	make_pw(l, arr);
}