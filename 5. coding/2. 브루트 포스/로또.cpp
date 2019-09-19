#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int i;

int main() {
    while(true) {
        int num;
        cin >> num;

        if (num == 0) break;

        vector<int> a(num);
        for (i = 0; i < num; i++) {
            cin >> a[i];
        }

        vector<int> v(6, 0);

        for (i = 0; i < num - 6; i++) {
            v.push_back(1);
        }

        do {
            for (i = 0; i < num; i++) {
                if (v[i] == 0) {
                    cout << a[i] << " ";
                }
            }
            cout << '\n';
        } while (next_permutation(v.begin(), v.end()));
        cout << '\n';
    }
    
}