#include <iostream>

using namespace std;

int main() {
	int aaa;
	int e, s, m;
	int x = 0, y = 0, z = 0;

	cin >> e >> s >> m;

	for (int i = 1; ; i++) {
		x++;
		y++;
		z++;
		if (x == 16)
			x = 1;
		if (y == 29)
			y = 1;
		if (z == 20)
			z = 1;
		if (e == x && s == y && m == z) {
			cout << i << '\n';
			break;
		}
	}
	cin >> aaa;
}