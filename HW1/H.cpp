#include <iostream>

using namespace std;

int main()
{
	int a, n1, b, n2;
	cin >> a >> b >> n1 >> n2;

	int t1_min = n1 * 1 + (n1 - 1) * a;
	int t1_max = n1 * 1 + (n1 + 1) * a;

	int t2_min = n2 * 1 + (n2 - 1) * b;
	int t2_max = n2 * 1 + (n2 + 1) * b;

	int t_min = max(t1_min, t2_min);
	int t_max = min(t1_max, t2_max);

	if (t_min > t_max)
		cout << -1;
	else
		cout << t_min << ' ' << t_max;
    return 0;
}