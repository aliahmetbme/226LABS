#include <iostream>

using namespace std;

int main() {
  int n;

  while (true) {
    cout << "Enter a positive integer greater than 1: ";
    cin >> n;
    if (n > 1) {
      break;
    }
    cout << "Invalid value. ";
  }

  int current = n;
  int steps = 0;

  while (current != 1) {
    if (steps == 0) {
      cout << current;
    }
    if (current % 2 == 0) {
      current /= 2;
    } else {
      current = current * 3 + 1;
    }
    cout << " -> " << current;
    steps++;
  }

  cout << "\nTotal steps: " << steps << "\n";

  return 0;
}