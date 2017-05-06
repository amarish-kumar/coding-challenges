#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

void solve();
void calc_primes();


int main(int argc, char* argv[]) {
	calc_primes();

	int t;
	cin >> t;
	while (t--)
		solve();

	return 0;
}

vector<short> primes;
const int MIN = 65;
const int MAX = 126;

void calc_primes() {
	for (short i = MIN; i <= MAX; i++ ) {
		bool prime = true;
		for (short j = 2; j <= (int)ceil(i / 2); j++ ) {
			if (i % j == 0) {
				prime = false;
				break;
			}
		}
		if (prime)
			primes.push_back(i);
	}
}

short nearest_prime(short i) {
	short np = 0;
	vector<short>::const_iterator it;
	short min_d = MAX + 1;

	for (it = primes.begin(); it < primes.end(); it++ ) {
		short dist = abs(i - *it);
		if (dist < min_d) {
			np = *it;
			min_d = dist;
		}
	}
	return np;
}

void solve() {
	int l;
	string s;
	cin >> l >> s;

	string::const_iterator it;
	for (it = s.begin(); it < s.end(); it++ ) {
		char c = (char)nearest_prime((short)*it);
		cout << c;
	}
	cout << endl;
}

