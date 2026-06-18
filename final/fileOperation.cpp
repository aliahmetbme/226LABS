#include <fstream>
#include <iostream>

using namespace std;

// int main() {

//   /*Declera file stream variables */

//   ifstream fIn;

//   ofstream fOn;

//   fstream boht;

//   fOn.open("deneme.txt");
//   if (!fOn.is_open()) {

//     cout << "Error opening file\n";
//     return 1;
//   }
//   fOn.write("Hello World", 11);
//   fOn.close();

//   fIn.open("deneme.txt");
//   char arr[100];
//   fIn.read(arr, 100);

//   cout << "\n" << arr;
//   fIn.close();

//   return 0;
// }

int main() {

  ofstream outFile("data.txt");

  if (!outFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  outFile << "Hello World";

  outFile.close();

  int count = 0;
  char ch;

  ifstream openFile("data.txt");

  while (!openFile.eof()) {
    openFile.get(ch);

    cout << ch;
  }

  openFile.close();
}