# Oto Galeri
import random

cars = ["bmw","mercedes","ford"]

while True:
  girdi = input("""
  1. Aracları Göster
  2. Araç Ekle
  3. Araç Sil
  4. Araç Öner
  5. Çıkış
  """)
  if girdi > "5" and girdi < "0":
    print("lütfen geçerli seçenek giriniz")

  elif girdi == "1":
    print(cars)

  elif girdi == "2":
    arac = input("lütfen yeni araç markası ekleyiniz")
    cars.append(arac)
  
  elif girdi == "3":
    silinen = input("silmek istediğiniz araç markasını giriniz")
    cars.remove(silinen)
  
  elif girdi == "4":
    print(random.choice(cars))
  
  elif girdi == "5":
    print("programdan çıkılıyor")
    break