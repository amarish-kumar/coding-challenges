#include <iostream>
#include <vector>

using namespace std;

void solve();
int calc_range(vector<int>::const_iterator&, vector<int>&);
void print_v(vector<int>&);


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

	vector<int> heights;
	while (n--) {
		int h;
		cin >> h;
		heights.push_back(h);
	}

	vector<int> ranges;

	vector<int>::const_iterator it;
	for (it = heights.begin(); it < heights.end(); it++) {
		int range = calc_range(it, ranges);
		ranges.push_back(range);
	}

	print_v(ranges);
}

int calc_range(vector<int>::const_iterator &tower, vector<int> &ranges) {
	int t_height = *tower;
	vector<int>::const_reverse_iterator rit(tower);
	vector<int>::const_reverse_iterator rngit = ranges.rbegin();

	int range = 1;

	while (rngit < ranges.rend()) {
		if (*rit > t_height)
			break;

		if (*rit == t_height) {
			range += *rngit;
			break;
		}

		range += *rngit;
		rit += *rngit;
		rngit += *rngit;
	}
	return range;
}

void print_v(vector<int> &v) {
	vector<int>::const_iterator it;
	for (it = v.begin(); it < v.end(); it++)
		cout << *it << " ";
	cout << endl;
}

