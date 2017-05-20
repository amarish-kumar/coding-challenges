#include <iostream>
#include <vector>

using namespace std;

void solve();


int main(int argc, char* argv[]) {
	int t;
	cin >> t;
	while (t--)
		solve();

	return 0;
}

void solve() {
	int n;
	cin >> n;

	int total_cs = 0;
	int total_n = 0;

	for(int i = 0; i < n; i++) {
		int n, cs;
		cin >> n >> cs;
		total_cs += cs;
		total_n += n;
	}
	
	cout << total_n - total_cs << endl;
}

