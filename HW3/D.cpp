#include <string>
#include <unordered_set>
#include <iostream>

using namespace std;

int main()
{
	unordered_set<string> set;
	string str;

	while (cin.peek() != EOF) {
		cin >> str;
		if (str.size() > 0)
			set.insert(str);
	}
	
	cout << set.size();

	return 0;
}