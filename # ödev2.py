# ödev2
# bir websitesi adresi geçerlmi değilmi
# yaşa göre ögrenim bilgisi
# kaçıncı aya göre mevsim
# kullanıcının hangi yolda olduğu (oto-köy-şehir içi) hız limiti
# kullanıcın kilometresi yağ lastik vb
# öğrencinin notuna göre puan kötü zayıf iyi pek iyi

"""
site = input("websitesi giriniz:")
if ".com" in site and "www." in site:
  print("geçerli websitesi")
else:
  print("geçersiz websitesi")
"""

"""
yas = input("yas giriniz")
if yas < 7:
  print("okula gidemez")
if yas >= 7 and yas <= 11:
  print("ilkokula gidiyor")
if yas > 11 and yas < 15:
  print("ortaokula gidiyor")
if yas >= 14 and yas <= 18:
  print("liseye gidiyor")
else:
  print("liseyi bitirmiş")
"""

"""
ay = int(input("kaçıncı ayda olduğunuzu giriniz"))
if ay == 12 or ay == 1 or ay == 2:
  print("kış mevsimindesiniz")
if ay == 3 or ay == 4 or ay == 5:
  print("ilkbahar mevsimindesiniz")
if ay == 6 or ay == 7 or ay == 8:
  print("yaz mevsimindesiniz")
if ay == 9 or ay == 10 or ay == 11:
  print("sonbahar mevsimindesiniz")
else:
  print("geçerli mevsim giriniz")
"""

"""
yol = input("hangi yol türündesiniz (otoyol-köy yolu-şehir içi yol")
if yol == "otoyol":
  print("hız sınırı 130 km/h")
if yol == "köy yolu":
  print("hız sınırı 50 km/h")
if yol == "şehir içi yol":
  print("hız sınırı 90 km/h")
else:
  print("lütfen verilen örnektekiler gibi yazınız")
"""

"""
km = int(input("arabanızın kilometresini giriniz:"))
if km < 10000:
  print("aracınıza bakım gerekmemektedir")
if km >= 10000 and km < 20000:
  print("aracınıza yağ yakıt polen hava filtreleri bakımı gerekmektedir")
if km >= 20000 and km < 60000:
  print("aracınıza buji değişimi alternatör kayışı değişimi ve otomatik şanzıman yağı değişimi bakımı yapılmalıdır")
if km >= 60000:
  print("aracınıza yağ filtreler fren balataları ve baskı balata kontrolleri yapılmalıdır")
"""

"""
puan = input("yazılıdan kaç not aldınız")
if puan <= 20 and puan >= 0:
  print("çok zayıf not aldınız")
if puan > 20 and puan < 50:
  print("zayıf not aldınız")
if puan == 50:
  print("geçer not aldınız")
if puan > 50 and puan <= 65:
  print("orta derecede not aldınız")
if puan > 65 and puan < 80:
  print("iyi not aldınız")
if puan >= 80 and puan < 95:
  print("çok iyi not aldınız")
if puan >= 95 and puan >= 100:
  print("pek iyi not aldınız")
else:
  print("lütfen geçerli bir not giriniz")
"""