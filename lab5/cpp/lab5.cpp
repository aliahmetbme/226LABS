#include <iostream>

double Sn(int n) {
  if (n <= 0) {
    return 0.0;
  }

  double sign = (n % 2 != 0) ? 1.0 : -1.0;

  double currentTerm = sign * (1.0 / n);

  return currentTerm + Sn(n - 1);
}

int main() {
  int n;

  std::cout << "S_n Serisinin Toplamini Hesaplama Programi" << std::endl;
  std::cout << "Lutfen pozitif bir 'n' degeri giriniz: ";
  std::cin >> n;

  if (n <= 0) {
    std::cout << "Lutfen gecerli (0'dan buyuk) bir deger giriniz." << std::endl;
    return 1;
  }

  double result = Sn(n);

  std::cout << "n = " << n << " icin S_n serisinin sonucu: " << result
            << std::endl;

  return 0;
}
