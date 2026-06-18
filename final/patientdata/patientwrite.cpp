#include <fstream> // Dosya işlemleri için kütüphane [cite: 249]
#include <iostream>

using namespace std;

int main() {
  // 1. Dosyaya yazmak için ofstream (output file stream) nesnesi
  // oluşturuyoruz.
  ofstream outFile("deskrelief_hastalar.txt");

  // 2. SINAVIN KRİTİK NOKTASI: Validation (Dosya açılabildi mi?)
  if (!outFile.is_open()) {
    cout << "Kritik Hata: Hasta veri dosyasi olusturulamadi!" << endl;
    return 1;
  }

  // 3. Dosyaya hasta verilerini yazdırıyoruz (tıpkı cout kullanır gibi).
  outFile << "ID: 3401, Isim: Ahmet Y., Teshis: Hipertansiyon, Risk: Yuksek\n";
  outFile << "ID: 3402, Isim: Ayse K., Teshis: Aritmi, Risk: Orta\n";
  outFile << "ID: 3403, Isim: Mehmet T., Teshis: Diyabet, Risk: Dusuk\n";

  cout << "Hasta verileri C++ tarafindan basariyla disa aktarildi." << endl;

  // 4. C++'ta dosyayı kapatmak ZORUNLUDUR.
  outFile.close();

  return 0;
}