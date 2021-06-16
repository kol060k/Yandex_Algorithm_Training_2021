#include <unordered_set>
#include <iostream>

using namespace std;

int main()
{
	unordered_set<int> columns;

	int n;
	cin >> n;

	int x, y;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		columns.insert(x);
	}

	cout << columns.size();

	return 0;
}