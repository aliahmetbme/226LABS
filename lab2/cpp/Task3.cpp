#include <iostream>

using namespace std;

int main() {
  int n;

  cout << "Enter a number between 3 and 9: ";
  cin >> n;

  while (n < 3 || n > 9) {
    cout << "Invalid input. Please enter a number between 3 and 9: ";
    cin >> n;
  }

  for (int i = 1; i <= 2 * n - 1; i++) {
    int k = n - abs(n - i);
    cout << string(k, '*') << "\n";
  }
  return 0;
}