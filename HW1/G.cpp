#include <iostream>

using namespace std;

int main()
{
	int N, K, m;
	cin >> N >> K >> m;
	int out = 0;
	int new_det;
	if (m > K)
		cout << 0;
	else {
		while (N >= K) {
			new_det = (N / K) * (K / m);
			out += new_det;
			N -= new_det * m;
		}
		cout << out;
	}

    return 0;
}