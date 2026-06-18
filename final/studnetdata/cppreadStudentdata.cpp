// cpp_read.cpp
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // 1. Dosyadan okuma yapmak için ifstream nesnesi oluşturuyoruz.
    // Python'un oluşturduğu aynı dosya adını veriyoruz.
    ifstream inFile("students_data.txt");
    string line;

    // 2. SINAVIN KRİTİK NOKTASI: Hata Kontrolü (Validation)
    // Dosya gerçekten açıldı mı? 
    if (!inFile.is_open()) {
        cout << "Hata: Dosya acilamadi veya bulunamadi!" << endl;
        return 1; // Programı hata koduyla bitir
    }

    cout << "--- C++ ile Dosyadan Okunan Veriler ---" << endl;

    // 3. Dosya sonuna gelene kadar (EOF) satır satır okuma yapıyoruz.
    while (getline(inFile, line)) {
        cout << line << endl;
    }

    // 4. C++'ta dosyayı manuel olarak kapatmak ZORUNLUDUR.
    inFile.close();
    
    return 0;
}