#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int t1, t2;
	cin >> t1;
	cin >> t2;
	string mode;
	cin >> mode;

	if (mode == "heat")
		cout << max(t1, t2);
	else if (mode == "freeze")
		cout << min(t1, t2);
	else if (mode == "auto")
		cout << t2;
	else
		cout << t1;
    return 0;
}