# Oto Galeri
import random

cars = ["bmw","mercedes","ford"]

def ekle():
    arac = input("lütfen yeni araç markası ekleyiniz")
    cars.append(arac)

def sil():
  silinen = input("silmek istediğiniz araç markasını giriniz")
  cars.remove(silinen)

def oner():
  print(random.choice(cars))

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
    ekle()
  elif girdi == "3":
    sil()
  elif girdi == "4":
    oner()
  elif girdi == "5":
    print("programdan çıkılıyor")
    break