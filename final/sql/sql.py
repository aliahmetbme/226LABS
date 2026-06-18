import mysql.connector

try:
    # 1. BAĞLANTIYI KURMA
    connection = mysql.connector.connect(
        host='localhost',
        database='MyNewDatabase',
        user='root',
        password='pass1234'
    )
    
    # Sütun isimleriyle (dictionary gibi) verilere erişmek için cursor'ı bu şekilde açıyoruz
    cursor = connection.cursor(dictionary=True)

    # ---------------------------------------------------------
    # GÖREV 1: ÖĞRENCİ BİLGİLERİ ÇEKME VE YAZDIRMA (SELECT)
    # ---------------------------------------------------------
    print("--- Tüm Öğrenciler ---")
    select_query = "SELECT * FROM Students"
    cursor.execute(select_query)
    
    records = cursor.fetchall()
    
    for row in records:
        # dictionary=True kullandığımız için sütun isimleriyle veriyi çekebiliyoruz
        id = row["Id"]
        name = row["Name"]
        score = row["Score"]
        print(id, name, score)

    # ---------------------------------------------------------
    # GÖREV 2: BELLİ BİR NOTUN ÜZERİNDE OLANLARI GÜNCELLEME (UPDATE)
    # ---------------------------------------------------------
    # Örnek: Notu 80 ve üzeri olan herkesin notunu 100 yap.
    update_query = "UPDATE Students SET Score = 100 WHERE Score >= 80"
    cursor.execute(update_query)
    
    # SINAVIN EN KRİTİK KODU: Değişiklik yaptıysan COMMIT etmek ZORUNDASIN!
    connection.commit()
    
    # Etkilenen (güncellenen) satır sayısını ekrana basma
    print(cursor.rowcount, "adet ogrencinin notu 100 olarak guncellendi.")

    # ---------------------------------------------------------
    # GÖREV 3: VERİ SİLME (DELETE)
    # ---------------------------------------------------------
    # Örnek: Notu 50 olan öğrencileri veritabanından sil.
    delete_query = "DELETE FROM Students WHERE Score = 50"
    cursor.execute(delete_query)
    connection.commit()
    print(cursor.rowcount, "adet ogrenci silindi.")

    # ---------------------------------------------------------
    # GÖREV 4: GÜVENLİ VERİ EKLEME (PARAMETERIZED INSERT)
    # ---------------------------------------------------------
    # Sınavda özellikle "parameterized" (parametre vererek) ekleme sorulur.
    insert_query = "INSERT INTO Students (Id, Name, Score) VALUES (%s, %s, %s)"
    new_student = (9000117, 'Ali Ahmet Erdogdu', 95) # Eklenecek veri 
    
    cursor.execute(insert_query, new_student)
    connection.commit()
    print("Yeni ogrenci basariyla eklendi.")

except mysql.connector.Error as e:
    # Herhangi bir SQL hatası olursa program çökmesin diye hatayı ekrana basıyoruz
    print("Veritabani hatasi olustu:", e) 

finally:
    # 5. BAĞLANTILARI KAPATMA (Temizlik Aşaması)
    if connection.is_connected(): 
        cursor.close() 
        connection.close() 
        print("MySQL baglantisi kapatildi.") 