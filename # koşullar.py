# koşullar
# Boolean veri tipi True-False 
"""
print(5>3)
print(5<3)
print(1 == 1)

if False:
  print("Çalıştı")

name = "ahmet"
if name == "furkan":
  print(name)

yas = int(input("yaşınızı giriniz:"))
if yas < 6:
  print("Ögrenci okula gitmiyor")
if yas > 6:
  print("Öğrenci herhangi bir okula gidiyor")

sayi = int(input("sayı giriniz:"))
if sayi < 0:
  print("negatif")
if sayi > 0:
  print("pozitif")
if sayi == 0:
  print("0")

sicaklik = int(input("Suyun sıcaklığını giriniz:"))
if sicaklik < 0:
  print("buz")
if sicaklik >= 0 and sicaklik < 100:
  print("sıvı")
if sicaklik >= 100:
  print("gaz")

mevsim = input("mevsim girin:")
saat = int(input("saat giriniz:"))
if mevsim == "yaz" and saat > 12:
  print("limonata")
if mevsim == "yaz" and saat <= 12:
  print("çay")
if mevsim == "ilkbahar":
  print("ayran")
if mevsim == "sonbahar":
  print("çay")
if mevsim == "kış":
  print("salep")

yas = int(input("yaşınızı giriniz"))
mezuniyet = input("mezuniyet derecenizi giriniz:")
if yas >= 18 and mezuniyet == "lise":
  print("sınava girebilir")
else:
  print("sınava giremez")

cinsiyet = input("cinsiyetinizi giriniz:")
yas = int(input("yasınızı giriniz:"))
if yas > 15 or cinsiyet == "erkek":
  print("kampa girebilir")
else:
  print("kampa giremez")

sayi = int(input("sayı giriniz"))
if not sayi > 0:
  print("sayı sıfırdan kucuktur")
else:
  print("sayı sıfırdan buyuktur")

buton = input("butona basınız")
basili = True
if basili == True:
  print("butona basıldı")
  basili = not basili
if basili == False:
  print("butona basılmadı")
  print(basili)

diploma = input("diplomanız varmı?")
tecrube = int(input("tecrubeniz kaç yıl?"))
if diploma == "var" and tecrube >= 5:
  print("işe alındınız")
else:
  print("işe alınamadınız")

if "f" in "furkan":
  print("çalıştı")
"""
mail = input("mail adresinizi giriniz:")
if "@" in mail and ".com" in mail:
  print("mail adresiniz geçerli")
else:
  print("mail adresiniz  geçersiz")