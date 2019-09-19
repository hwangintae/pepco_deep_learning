#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;
	for (int i = 0; i < num; i++) {
	int ln = 0;
	int n;
	cin >> n;
	for (int l0 = 1; l0 <= 3; l0++){
		if (l0 == n) ln++;
		for (int l1 = 1; l1 <= 3; l1++){
			if (l0 + l1 == n) ln++;
			for (int l2 = 1; l2 <= 3; l2++){
				if (l0 + l1 + l2== n) ln++;
				for (int l3 = 1; l3 <= 3; l3++){
					if (l0 + l1 + l2 + l3 == n) ln++;
					for (int l4 = 1; l4 <= 3; l4++){
						if (l0 + l1 + l2 + l3 + l4 == n) ln++;
						for (int l5 = 1; l5 <= 3; l5++){
							if (l0 + l1 + l2 + l3 + l4 + l5 == n) ln++;
							for (int l6 = 1; l6 <= 3; l6++){
								if (l0 + l1 + l2 + l3 + l4 + l5 + l6 == n) ln++;
								for (int l7 = 1; l7 <= 3; l7++){
									if (l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 == n) ln++;
									for (int l8 = 1; l8 <= 3; l8++){
										if (l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 == n) ln++;
										for (int l9 = 1; l9 <= 3; l9++){
											if (l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 == n) ln++;
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	cout << ln << '\n';
	}		
}