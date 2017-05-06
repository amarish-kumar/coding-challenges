#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void solve();


int main(int argc, char* argv[]) {
	solve();
	return 0;
}

struct City;

struct Road {
	City* city;
	int p;

	Road(City* c, int ps) {
		city = c;
		p = ps;
	}
};

struct City {
	int number;
	vector<Road> roads;

	City(int n) {
		number = n;
	}

	void link(City* c, int p) {
		roads.push_back(Road(c, p));
	}
};

// make a map (graph) of cities connected by roads
vector<City*>* make_map() {
	int n, r;
	cin >> n >> r;

	vector<City*> *cities = new vector<City*>();
	for (int i = 1; i <= n; i++)
		cities->push_back(new City(i));

	for (int i = 0; i < r; i++) {
		int c1, c2, p;
		cin >> c1 >> c2 >> p;
		cities->at(c1 - 1)->link(cities->at(c2 - 1), p);
	}
	return cities;
}

struct {
	vector<int> path;
	int trips;
} solution;


void traverse(City*, City*, int, int, vector<int>&);


void solve() {
	vector<City*> *cities = make_map();

	int s, d, t;
	cin >> s >> d >> t;

	solution.trips = t + 1;
	City* start = cities->at(s - 1);
	City* dest = cities->at(d - 1);

	vector<int> path;
	path.push_back(s);

	traverse(start, dest, t, 0, path);

	//print solution
	vector<int>::const_iterator it;
	for (it = solution.path.begin(); it < solution.path.end(); it++)
		cout << *it << " ";
	cout << endl;
	cout << solution.trips << endl;

	//free memory
	vector<City*>::const_iterator ct;
	for (ct = cities->begin(); ct < cities->end(); ct++)
		delete(*ct);
	cities->clear();
	delete cities;
}

void traverse(City* current, City* dest, int tourists, int max_trips, vector<int> &path) {
	if (current == dest) {
		if (max_trips < solution.trips) {
			solution.path = path;
			solution.trips = max_trips;

		} else if (max_trips == solution.trips) {
			bool less = lexicographical_compare(path.begin(), path.end(), solution.path.begin(),
					solution.path.end());
			if (less) {
				solution.path = path;
				solution.trips = max_trips;
			}
		}
		return;
	}

	vector<Road>::const_iterator road;

	for (road = current->roads.begin(); road < current->roads.end(); road++) {
		if (road->p > tourists)
			continue;

		max_trips = max(max_trips, (int)ceil((float)tourists / (road->p - 1)));
		path.push_back(road->city->number);
		traverse(road->city, dest, tourists, max_trips, path);
		path.pop_back();
	}
}

