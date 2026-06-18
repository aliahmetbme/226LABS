with open("deneme.txt", "w") as f:
    f.write("Hello World");
    f.close();

with open("text.txt","w") as f:
    f.write("This will be my first line \n this gonna be second")
    f.close() 

try:
    f = open("text.txt","r")
    print(f.read())
finally:
    f.close() 

with open("text.txt","w") as f:
    #f.write("this is my third line \n")
    x = 10
    f.write(str(x))
    f.close() 


myObject = open ("myfile.txt","w") 
lines = ["Hello everyone\n", "writing multiline strings\n","using file methods\n","is fun!"]
myObject.writelines(lines)
myObject.close()



with open("myfile.txt","a") as f:
    lines = ["Hello everyone\n", "writing multiline strings\n","using file methods\n","is fun!"]
    f.writelines(lines)
    f.close()

import numpy as np 

myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

with open("numpy_data.txt","w+") as f:
    
    content = "\n".join([str(i) for i in myArray])
    f.write(content)
    f.close()

    file = open("numpy_data.txt","r")
    content =  file.read()  
    file.close()  

    print ("\n Array content:\n", content)


# Dosya içeriği: 
# Yazılım Muhendisligi
# Ileri Programlama

with open("test.txt", "r") as f:
    # --- read(n) Mantığı ---
    # İmleç 0. pozisyonda. 10 karakter oku, imleç 10. pozisyona gitsin.
    part1 = f.read(10) 
    print(f"Okunan kısım (10 karakter): {part1}")
    
    # İmleç şu an 10. pozisyonda. Parametre yoksa, imleçten başla sonuna kadar oku.
    remaining = f.read()
    print(f"Kalan kısım: {remaining}")
    
    # Not: Bu noktada imleç dosyanın sonuna geldi.
    # Eğer burada tekrar f.read() deseydin, boş bir string ('') dönerdi.

# --- readline() ve readline(n) Mantığı ---
with open("test.txt", "r") as f:
    # 1. satırı oku. İmleç 1. satırın sonuna (\n) geldi, okudu ve 2. satırın başına geçti.
    line1 = f.readline() 
    print(f"\n1. Satır: {line1.strip()}")
    
    # 2. satırın başındayız. Sadece 5 karakter oku.
    # İmleç 5. karakterin (İ, l, e, r, i) hemen sonrasında bekliyor.
    partial_line = f.readline(5)
    print(f"2. satırdan 5 karakter: {partial_line}")
    
    # Şimdi readline() dersek, kaldığı yerden (yani 'i' harfinden) satır sonuna kadar okur.
    rest_of_line = f.readline()
    print(f"Aynı satırın kalanı: {rest_of_line.strip()}")


# --- readlines() Mantığı ---
# Dosyayı "okuma" (read) modunda açıyoruz
with open("test.txt", "r") as f:
    print("\n--- readlines() sonucu ---")
    
    # readlines() imlecin bulunduğu noktadan itibaren dosyanın sonuna kadar olan 
    # TÜM satırları okur ve RAM belleğe yükler.
    # Her bir satır sonundaki '\n' dahil olacak şekilde bir listenin elemanı olur.
    # Dosya çok büyükse RAM'i doldurabileceği için dikkatli kullanılmalıdır!
    lines = f.readlines() 
    
    # lines değişkeninin bir Python listesi (<class 'list'>) olduğunu doğrularız
    print("Veri tipi:", type(lines)) 
    
    # Listenin ham halini ekrana yazdırırız.
    # Çıktı: ['Yazılım Muhendisligi\n', 'Ileri Programlama\n', ...]
    print("Liste içeriği:", lines)
    
    # Döngü kurarak her bir satırı (listenin her bir elemanını) tek tek işleyebiliriz.
    for l in lines:
        # l değişkeni her bir satırı ('Yazılım Muhendisligi\n' gibi) tutar.
        # .strip() komutu satırın sağındaki ve solundaki boşlukları (ve \n karakterini) siler.
        # Böylece alt alta yazdırırken fazladan boşluk oluşmaz.
        print("Satir:", l.strip())

print("\n# --- tell() ve seek() Mantığı ---")
print("Learning to move the file object")

# Dosyayı okuma modunda açıyoruz. İmleç başlangıçta (0. pozisyonda) durur.
fileobject=open("myfile.txt","r")

# Dosyanın TÜM içeriğini okuyoruz. Bu işlem sonucunda imleç (file pointer) 
# karakterleri okuyarak dosyanın en sonuna kadar ilerlemiş olur.
str_content=fileobject.read()
print(str_content)

# tell() fonksiyonu bize imlecin o an hangi byte (karakter) pozisyonunda olduğunu söyler.
# Tüm dosyayı okuduğumuz için imleç dosyanın en sonundadır (dosyanın toplam boyutu kadar bir sayı döner).
print("Initially, the position of the file object is: ",fileobject.tell())

# seek(0) fonksiyonu imleci istediğimiz pozisyona taşır. Burada 0 diyerek 
# imleci dosyanın en başına (0. pozisyona) geri sarmış oluyoruz.
fileobject.seek(0)

# İmleci başa sardığımız için tell() fonksiyonu şimdi bize tekrar 0 değerini verecektir.
print("Now the file object is at the beginning of the file:",fileobject.tell())

# seek(10) ile imleci dosyanın başından itibaren 10 byte (karakter) ileri taşıyoruz.
fileobject.seek(10)
print("We are moving to 10th byte position from the beginning of file")

# tell() ile kontrol ettiğimizde imlecin 10. pozisyonda olduğunu görürüz.
print("The position of the file object is at", fileobject.tell())

# Şimdi okuma (read) yaparsak, dosyanın başından değil, imlecin şu an bulunduğu 
# 10. pozisyondan başlayarak dosyanın sonuna kadar olan kısmı okur. 
# Yani ilk 10 karakteri atlamış oluruz.
str_content=fileobject.read()
print(str_content)