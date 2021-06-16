#include <iostream>

using namespace std;

int main()
{
	int t1, t2, t3;
	cin >> t1 >> t2 >> t3;
	if ((t1 + t2 > t3) && (t1 + t3 > t2) && (t2 + t3 > t1))
		cout << "YES";
	else
		cout << "NO";
    return 0;
}