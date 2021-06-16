#include <string>
#include <iostream>

using namespace std;

string get_num() {
	string num = "";
	string temp;
	cin >> temp;
	for (int i = 0; i < temp.length(); i++) {
		if (temp[i] == '+') {
			i++;
			num += '8';
		}
		else if ((temp[i] >= '0') && (temp[i] <= '9'))
			num += temp[i];
	}
	if (num.length() == 7)
		return "8495" + num;
	else if (num.length() == 8) {
		string answer = "8495";
		for (int i = 1; i < num.length(); i++)
			answer += num[i];
		return answer;
	}
	else
		return num;
}

int main()
{
	string new_num = get_num();
	string arr[3];
	for (int i = 0; i < 3; i++) {
		arr[i] = get_num();
	}
	for (int i = 0; i < 3; i++)
		if (arr[i] == new_num)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
    return 0;
}