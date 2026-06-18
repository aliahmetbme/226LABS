# python_reader.py
# Amacımız: C++'ın oluşturduğu hasta dosyasını okuyup ekrana düzenli basmak.

print("--- Python Klinik Veri Analizi ---")

try:
    # 1. 'r' (read) modu ile okuma yapıyoruz. 'with' bloğu dosyayı otomatik kapatır[cite: 59, 131].
    with open("deskrelief_hastalar.txt", "r") as f:
        
        # 2. Dosya üzerinde döngü kurarak satır satır okuma işlemi yapıyoruz[cite: 201].
        for line in f:
            # .strip() ile C++'ın eklediği satır sonu boşluklarını (\n) temizliyoruz.
            hasta_kaydi = line.strip()
            
            # Sınavda ekstra puan getirecek küçük bir analiz mantığı:
            if "Yuksek" in hasta_kaydi:
                print(f"⚠️ ACIL DURUM: {hasta_kaydi}")
            else:
                print(f"Normal Kayit: {hasta_kaydi}")

except FileNotFoundError:
    print("Hata: Hasta veri dosyasi bulunamadi! Lutfen once C++ kodunu calistirin.")