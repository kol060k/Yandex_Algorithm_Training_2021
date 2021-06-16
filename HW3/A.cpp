#include <unordered_set>
#include <iostream>

using namespace std;

int main()
{
	unordered_set<int> set;
	int n;
	while (cin.peek() != '\n' && cin.peek() != EOF) {
		cin >> n;
		set.insert(n);
	}
	cout << set.size();
	return 0;
}