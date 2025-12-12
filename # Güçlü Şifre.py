# Güçlü Şifre
sifre = input("sifre giriniz")

sayi = 0
kucuk = 0
buyuk = 0
ozel = 0

for harf in sifre:
  # print(harf)
  
  if harf.isdigit():
    sayi += 1
  elif harf.islower():
    kucuk += 1
  elif harf.isupper():
    buyuk += 1
  elif not harf.isalnum():
    ozel += 1

if len(sifre) < 8:
  print("zayıf şifre")
elif sayi < 2 or kucuk < 2 or buyuk < 2 or ozel < 2:
  print("zayıf şifre")
else:
  print("güçlü şifre")