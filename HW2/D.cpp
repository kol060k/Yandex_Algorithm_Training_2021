#include <iostream>

using namespace std;

int main()
{
	int num, old_num, very_old_num;
	int big_elem = 0;
	if (cin.peek() == '\n' && cin.peek() == EOF) {
		cout << 0;
		return 0;
	}
	cin >> very_old_num;
	if (cin.peek() == '\n' && cin.peek() == EOF) {
		cout << 0;
		return 0;
	}
	cin >> old_num;
	while (cin.peek() != '\n' && cin.peek() != EOF) {
		cin >> num;
		if (old_num > very_old_num && old_num > num)
			big_elem++;
		very_old_num = old_num;
		old_num = num;
	}
	cout << big_elem;
	return 0;
}