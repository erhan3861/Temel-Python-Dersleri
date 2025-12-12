# ödev3
# ralli 1 2 3 turda tamamlama süresi float ortalama süresi
# otobüs kaç durak gittiği durakları ortalama gitme süresi dakika (toplam mesafe) ve 2 durak mesafesi
# bir uçağın yakıtı bir litre ne kadar süre gider full yakıtla ne kadar gidebilir
# bir yerin şehire olan uzaklığı 1km sehir 10km kasaba 100km köy
# bir yerin nüfusu 1000köy 10000ilçe 1000000şehir 1000000büyük şehir

"""
sure1 = float(input("1. tur tamamlama surenizi giriniz"))
sure2 = float(input("2. tur tamamlama surenizi giriniz"))
sure3 = float(input("3. tur tamamlama surenizi giriniz"))
print("ralli yarışında her turu ortalama geçme süreniz:" , sure1 / 3 + sure2 / 3 + sure3 / 3)
"""

"""
durak = int(input("kaç durak gidiyorsunuz"))
sure = int(input("kaç dakikada gidiyorsunuz"))
mesafe2 = int(input("2 durak arası mesafe kaç metre"))
print("duraklar arası ortalama sureniz" , sure / durak , "dakikadır")
print("toplam mesafe" , mesafe2 * durak / 2)
"""

"""
mesafe = int(input("uçakla 1 litre yakıtla kaç dakika gidebiliyorsunuz?"))
print("uçak ile full depoyla" , mesafe * 125000 / 60 , "saat gidebilirsiniz")
"""

"""
mesafe = int(input("yaşadığınız yerin şehire mesafesi kaç km"))
if mesafe >= 1 and mesafe > 0:
  print("yaşadığınız yer bir şehirdir")
elif mesafe >= 10:
  print("yaşadığınız yer bir kasabadır")
elif mesafe >= 100:
  print("yaşadığınız yer bir köydür")
else:
  print("doğru sayı giriniz")
"""

"""
nufus = int(input("yaşadığınız yerin nufusunu giriniz"))
if nufus >= 1000 and nufus > 0:
  print("yaşadığınız yer bir köydür")
elif nufus >= 10000:
  print("yaşadığınız yer bir ilçe")
elif nufus >= 100000:
  print("yaşadığınız yer bir şehir")
elif nufus >= 1000000:
  print("yaşadığınız yer bir büyük şehir")
else:
  print("dogru nüfüs giriniz")
"""