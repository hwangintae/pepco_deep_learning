#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int w[9];
	int all = 0;

	for (int i = 0; i < 9; i++) {
		cin >> w[i];
		all += w[i];
	}
	sort(w, w+9);
	for (int i = 0; i < 9; i++) {
		for(int j = 1 + i; j < 9; j++) {
			if (all - w[i] - w[j] == 100) {
				for (int k = 0; k < 9; k++) {
					if (i == k || j == k) continue;
					cout << w[k] << '\n';
				
				}
				return 0;
			}
		}
	}
	return 0;
}