#include <iostream>

using namespace std;

int main()
{
	int num, old_num;
	bool ordered = true;
	cin >> old_num;
	while (cin.peek() != '\n' && cin.peek() != EOF) {
		cin >> num;
		if (num <= old_num)
			ordered = false;
		old_num = num;
	}
	if (ordered)
		cout << "YES";
	else
		cout << "NO";

	return 0;
}