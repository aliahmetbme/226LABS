#include <cmath>    // math functions
#include <iostream> // input output

using namespace std;

int main() {

  string name;
  string id;

  cout << "What is your name?\n";
  getline(cin, name); // allows to enter spaces
  cout << "Hello " << name << ".\n";
  cout << "\n";
  cout << name << endl;
  cout << "What is your Student ID?\n";
  cin >> id;
  cout << "Your ID is " << id << ".\n";
  cout << id << endl;

  int second;

  cout << "Enter a value in seconds: \n";
  cin >> second;

  int hours = second / 3600;
  int minutes = (second % 3600) / 60;
  int seconds = second % 60;

  cout << second << " seconds is equal to " << hours << " : " << minutes
       << " : " << seconds << "\n";

  int x1, y1, x2, y2;

  cout << "Enter the coordinates of the first point:\n";
  cin >> x1 >> y1; // getting two inputs at a same time
  cout << "Enter the coordinates of the second point:\n";
  cin >> x2 >> y2;
  cout << "The distance between the two points is: ";
  cout << sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) << "\n";

  cout << "\n";

  cout << "*******\n" << " *****\n" << "  ***\n" << "   *\n";

  return 0;
}
