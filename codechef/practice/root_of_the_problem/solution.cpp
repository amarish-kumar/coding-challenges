#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

void solve();
int make_tree(map<int, int>&, vector<int>&);

#define pvi(MSG, V) 	cout << MSG; \
			for(vector<int>::const_iterator it = V.begin(); it < V.end(); it++) \
				cout << *it << " "; \
			cout << endl; \



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

	map<int, int> nodes;
	int max_cs = 0;
	int max_n = 0;

	for(int i = 0; i < n; i++) {
		int n, cs;
		cin >> n >> cs;
		nodes[n] = cs;
		max_cs = max(max_cs, cs);
		max_n = max(max_n, n);
	}
	if (max_n > max_cs) {
		cout << max_n << endl;
		return;
	}

	vector<int> used;
	int root = make_tree(nodes, used);
	cout << root << endl;
}

bool is_valid_node(map<int, int> &nodes, int v) {
	for(map<int, int>::iterator it = nodes.begin(); it != nodes.end(); it++)
		if (it->first == v)
			return true;
	return false;
}

bool is_used(vector<int> &used, int v) {
	return find(used.begin(), used.end(), v) != used.end();
}

int make_tree(map<int, int> &nodes, vector<int> &used) {
	//pvi("used: ", used);

	if (used.size() == 0) {
		map<int, int>::iterator it;
		for(it = nodes.begin(); it != nodes.end(); it++) {
			int root = it->first;
			used.push_back(root);

			int r = make_tree(nodes, used);
			if ((used.size() == nodes.size()) && (r > -1))
				return root;

			used.clear();
		}
	} else {
		int parent = used.back();
		int c_sum = nodes[parent];

		if (c_sum == 0)
			return 1;

		int r = -1;
		for(int i = 0; i <= (int)(c_sum / 2); i++) {
			int c1, c2;
			c1 = i;
			c2 = c_sum - i;

			//cout << "c1c2: " << c1 << ", " << c2 << endl;

			if (!is_used(used, c1) && !is_used(used, c2)) {
				if (c1 != 0 && !is_valid_node(nodes, c1))
			       		continue;
				if (c1 > 0) {
					used.push_back(c1);
					r = make_tree(nodes, used);
				}
				if (is_valid_node(nodes, c2)) {
					used.push_back(c2);
					r = make_tree(nodes, used);
				}
			}

			if (r > -1)
				return r;
		}
		return r;
	}
}

