#include <iostream>
#include <vector>

using namespace std;

struct frnd;
frnd* read_f_list(int);
frnd* remove_f(frnd*, int);
void print_f(frnd const *);
void del_f_list(frnd*);


struct frnd {
	int pop;
	frnd* next;
};

// class to maintain a fixed size stack
class Stack {
	private:
		vector<frnd*> v;
		int max_size;

	public:
		Stack(int size) {
			max_size = size;
		}

		void push(frnd* p) {
			v.push_back(p);
			if (v.size() > max_size)
				v.erase(v.begin());
		}

		frnd* pop() {
			frnd* p = v.back();
			v.pop_back();
			return p;
		}

		void change_size(int size) {
			max_size = size;
		}

		void clear() {
			v.clear();
		}
		
		bool empty() {
			return v.size() == 0;
		}
};

int main(int argc, char* argv[]) {
	int t;
	cin >> t;
	while (t--) {
		int n, k;
		cin >> n >> k;
		frnd* f = read_f_list(n);
		f = remove_f(f, k);
		print_f(f);
		del_f_list(f);
	}

	return 0;
}

frnd* read_f_list(int n) {
	frnd* lf = NULL;
	frnd* head = NULL;

	while (n--) {
		frnd* nf = new frnd();
		cin >> nf->pop;
		if (lf)
			lf->next = nf;
		else
			head = nf;
		nf->next = NULL;
		lf = nf;
	}
	return head;
}

frnd* remove_f(frnd* head, int k) {
	frnd *p0, *p1, *p2;

	p0 = NULL;
	p1 = head;
	p2 = head->next;

	Stack back = Stack(k);
	bool frnd_deleted = false;

	while (k > 0) {
		if (p1 == NULL)
			return NULL;

		if (p2 == NULL) {
			if (!frnd_deleted) {
				delete p1;
				p0->next = NULL;
				k--;
			}

			p0 = NULL;
			p1 = head;
			p2 = head->next;
			frnd_deleted = false;

			continue;
		}

		if (p1->pop < p2->pop) {
			delete p1;
			frnd_deleted = true;
			k--;

			if (back.empty()) {
				head = p2;
				p1 = p2;
				p2 = p2->next;
			} else {
				p0 = back.pop();
				p0->next = p2;
				p1 = p0;
			}
		} else {
			back.push(p1);
			p1 = p2;
			p2 = p2->next;
		}
	}
	return head;
}

void print_f(frnd const *f) {
	while (f != NULL) {
		cout << f->pop << " ";
		f = f->next;
	}
	cout << endl;
}

void del_f_list(frnd* head) {
	while (head != NULL) {
		frnd* tmp = head;
		head = head->next;
		delete tmp;
	}
}

