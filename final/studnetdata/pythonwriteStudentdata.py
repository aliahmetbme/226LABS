# python_write.py
# Amacımız: "students_data.txt" adında bir dosya oluşturup içine veri yazmak.

# 'w' modu dosyayı yazma modunda açar (dosya yoksa oluşturur, varsa içini sıfırlar).
with open("students_data.txt", "w") as file:
    # f.write() ile satır satır verilerimizi yazıyoruz. Satır sonlarına \n koymayı unutmuyoruz[cite: 69].
    file.write("ID: 101, İsim: Ali, Not: 85\n")
    file.write("ID: 102, İsim: Ayşe, Not: 92\n")
    file.write("ID: 103, İsim: Mehmet, Not: 78\n")

print("Veriler Python ile dosyaya basariyla yazildi!")