#include <iostream>

using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;
	if (c < 0)
		cout << "NO SOLUTION";
	else {
		if (a == 0) {
			if (b == c * c)
				cout << "MANY SOLUTIONS";
			else
				cout << "NO SOLUTION";
		}
		else {
			double ans = (c*c - b) / a;
			if (ans * a != c * c - b)
				cout << "NO SOLUTION";
			else
				cout << ans;
		}
	}
    return 0;
}