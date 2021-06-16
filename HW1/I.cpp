#include <iostream>

using namespace std;

int main()
{
	int kirp[3], hole[2];
	cin >> kirp[0] >> kirp[1] >> kirp[2] >> hole[0] >> hole[1];

	int flag = 0;
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 2; j++)
			if ((kirp[i] <= hole[j]) && (kirp[(i + 1) % 3] <= hole[(j + 1) % 2]))
				flag = 1;

	if (flag == 1)
		cout << "YES";
	else
		cout << "NO";

    return 0;
}