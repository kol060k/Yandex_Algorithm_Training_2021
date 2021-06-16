#include <iostream>

using namespace std;

int main()
{
	int n1[2], n2[2];
	cin >> n1[0] >> n1[1] >> n2[0] >> n2[1];
	int mult = 0;
	int best_l, best_w;

	// Расположим ноутбуки рядом: □□ и будем их поворачивать вокруг своей оси
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			int square = max(n1[i], n2[j]) * (n1[(i + 1) % 2] + n2[(j + 1) % 2]);
			if ((square < mult) || (mult == 0)) {
				best_l = max(n1[i], n2[j]);
				best_w = n1[(i + 1) % 2] + n2[(j + 1) % 2];
				mult = square;
			}
		}
	}
	cout << best_l << ' ' << best_w;

    return 0;
}