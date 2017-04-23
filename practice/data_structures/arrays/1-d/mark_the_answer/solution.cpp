#include <iostream>
#include <vector>

using namespace std;


void read_array(vector<int>&, int);
int solve(const vector<int>&, int);


int main(int argc, char* argv[]) {
	int n, x;
	cin >> n >> x;
	vector<int> v;
	read_array(v, n);
	int r = solve(v, x);
	cout << r << endl;

	return 0;
}

void read_array(vector<int>& v, int n) {
	int i;
	while (n--) {
		cin >> i;
		v.push_back(i);
	}
}

int solve(const vector<int>& v, int x) {
	int max_score = 0;
	vector<int>::const_iterator it;
	bool skipped = false;
	int score = 0;

	for (it = v.begin(); it < v.end(); it++) {
		if (*it <= x)
			score++;
		else
			if (skipped) {
				max_score = max(score, max_score);
				break;
			} else
				skipped = true;
	}
	max_score = max(score, max_score);
	return max_score;	
}

