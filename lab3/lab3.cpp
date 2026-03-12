#include <iostream>

using namespace std;

// Swaps the values of two integers using pointers.
void swapValues(int *p1, int *p2) {
  int temp = *p1;
  *p1 = *p2;
  *p2 = temp;
}

// Prints the elements of an array using pointer notation.
void printArray(int *arr, int size) {
  for (int i = 0; i < size; i++) {
    cout << *(arr + i) << " ";
  }
  cout << endl;
}

// Returns the sum of the array elements.
int findSum(int *arr, int size) {
  int sum = 0;
  for (int i = 0; i < size; i++) {
    sum += *(arr + i);
  }
  return sum;
}

// Shifts all elements of the array one position to the right.
void shiftRight(int *arr, int size) {
  if (size <= 1)
    return;
  int last = *(arr + size - 1);
  for (int i = size - 1; i > 0; i--) {
    *(arr + i) = *(arr + i - 1);
  }
  *arr = last;
}

// Dynamically creates an integer array and returns its address.
int *createArray(int size) { return new int[size]; }

// Frees the dynamically allocated memory.
void deleteArray(int *arr) { delete[] arr; }

int main() {
  cout << "Creating dynamic array..." << endl;

  int size;
  cout << "Enter array size: ";
  cin >> size;

  int *arr = createArray(size);

  cout << "Enter values: ";
  for (int i = 0; i < size; i++) {
    cin >> *(arr + i);
  }
  cout << endl;

  cout << "Array elements:" << endl;
  printArray(arr, size);

  cout << "Sum of elements: " << findSum(arr, size) << endl;

  cout << "----------------------------------" << endl;
  cout << "Shifting array to the right..." << endl;
  shiftRight(arr, size);
  cout << "Array after shiftRight:" << endl;
  printArray(arr, size);

  cout << "----------------------------------" << endl;
  cout << "Swapping two numbers" << endl;
  int a, b;
  cout << "Enter values for a and b: ";
  cin >> a >> b;

  cout << "Before swap" << endl;
  cout << "a = " << a << endl;
  cout << "b = " << b << endl;

  swapValues(&a, &b);

  cout << "After swap" << endl;
  cout << "a = " << a << endl;
  cout << "b = " << b << endl;

  cout << "----------------------------------" << endl;
  cout << "Deleting array..." << endl;
  deleteArray(arr);
  cout << "Memory released successfully." << endl;

  return 0;
}
