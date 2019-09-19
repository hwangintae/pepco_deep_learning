#include <iostream>

using namespace std;

int GCD(int x, int y) {
	if (y == 0) {
		return x;
	}
	else {
		GCD(y, x%y);
	}
}

int main() {
	int num, x, y;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> x >> y;
		cout << x * y / GCD(x, y) << '\n';
	}
}