#include <vector>
#include <iostream>

using namespace std;

int main()
{
	vector<int> numbers(10);

	for (int i = 0; i < 10; i++)
		numbers[i] = 0;

	int x, y, z;
	cin >> x >> y >> z;
	numbers[x] = 1;
	numbers[y] = 1;
	numbers[z] = 1;

	char c;
	int k = 0;
	 do {
		cin >> c;
		if (numbers[c - '0'] == 0) {
			numbers[c - '0'] = 2;
			k += 1;
		}
	 } while (cin.peek() != '\n' && cin.peek() != EOF);

	cout << k << endl;

	return 0;
}