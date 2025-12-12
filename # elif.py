# elif
"""
yas = int(input("yas giriniz"))
if yas < 7:
  print("okula gidemez")
elif yas <= 11:
  print("ilkokula gidiyor")
elif yas <= 15:
  print("ortaokula gidiyor")
elif yas <= 18:
  print("liseye gidiyor")
else:
  print("liseyi bitirmiş")
"""

"""
puan = int(input("yazılıdan kaç not aldınız"))
if puan <= 20 and puan >= 0:
  print("çok zayıf not aldınız")
elif puan < 50:
  print("zayıf not aldınız")
elif puan == 50:
  print("geçer not aldınız")
elif puan <= 65:
  print("orta derecede not aldınız")
elif puan <= 80:
  print("iyi not aldınız")
elif puan <= 95:
  print("çok iyi not aldınız")
elif puan == 100:
  print("pek iyi not aldınız")
else:
  print("lütfen geçerli bir not giriniz")
"""

"""
sicaklik = int(input("sıcaklık giriniz"))
if sicaklik < 0:
  print("soğuk")
elif sicaklik <=30:
  print("ılık")
elkey = input("tuş giriniz")
if key == "w":
  print("ileri")
elif key == "a":
  print("sol")
elif key == "d":
  print("sağ")
elif key == "s":
  print("geri")
elif key == "space":
  print("zıplama")
"""

"""
kup = int(input("elinizdeki küp sayısını giriniz"))
if kup <= 10:
  print("duvar")
elif kup <= 100:
  print("kulübe")
elif kup <= 1000:
  print("ev")
elif kup <= 10000:
  print("apartman")
"""

"""
sure = int(input("çalıştığınız süreyi giriniz"))
if sure > 0 and sure / 60 < 1:
  print("yeterli sürede çalışmadınız" , 60 - sure , "dakika daha çalışmalısınız")
elif sure / 60 > 1:
  print("fazladan çalıştınız çalıştığınız ekstradan süre =" , sure - 60 , "dakikadır")
elif sure == 60:
  print("yeterli")
else:
  print("doğru süre giriniz")
"""

"""
kira = int(input("kaç dakika kiraladığınızı giriniz"))
if kira <= 180 and kira > 0:
  print("toplam ücretiniz" , kira * 100 / 60)
elif kira <= 300:
  print("toplam ücretiniz" , kira * 90 / 60)
elif kira <= 480:
  print("toplam ücretiniz" , kira * 80 / 60)
elif kira > 480:
  print("toplam ücretiniz" , kira * 70 / 60)
"""

"""
benzin = float(input("arabanızda kaç litre benzin kaldığını giriniz"))
print("arabanızla" , benzin * 10 ,"kilometre daha gidebilirsiniz")
"""
"""
bahce = input("bahçenizin şeklini giriniz")
agac = int(input("kaç tane ağaç dikmek istiyorsunuz"))
if bahce == "kare":
  print("bahçenize" , 40 / agac ,"metre arayla ağaç dikebilirsiniz")
if bahce == "üçgen":
  print("bahçenize" , 30 / agac ,"metre arayla ağaç dikebilirsiniz")
if bahce == "beşgen":
  print("bahçenize" , 50 / agac ,"metre arayla ağaç dikebilirsiniz")
se:
  print("sıcak")
"""