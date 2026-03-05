#include <iostream>

using namespace std;

int main() {
  int n = 0; // Initialize n to 0 for the first prompt condition

  while (true) {
    if (n == 0) { // İlk mesaj
      cout << "Please enter a number between 10 and 100: ";
    } else {
      cout << "Invalid input. Please enter a number between 10 and 100: ";
    }

    cin >> n;

    if (n >= 10 && n <= 100) {
      break;
    }
  }

  int fizzCount = 0;
  int buzzCount = 0;
  int fizzBuzzCount = 0;

  for (int i = 1; i <= n; i++) {
    if (i % 7 == 0) {
      cout << "(" << i << " is skipped)\n";
      continue;
    } else if (i % 3 == 0 && i % 5 == 0) {
      cout << "FizzBuzz\n";
      fizzBuzzCount++;
    } else if (i % 3 == 0) {
      cout << "Fizz\n";
      fizzCount++;
    } else if (i % 5 == 0) {
      cout << "Buzz\n";
      buzzCount++;
    } else {
      cout << i << "\n";
    }
  }

  cout << "--- Summary ---\n";
  cout << "Fizz count : " << fizzCount << "\n";
  cout << "Buzz count : " << buzzCount << "\n";
  cout << "FizzBuzz count: " << fizzBuzzCount << "\n";

  return 0;
}