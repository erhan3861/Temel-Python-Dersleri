# Değişkenler
#kurallar
#1Değişkenler rakam ve özel işaretle başlamaz
#2Değişkenlerde boşluk olmaz
#3Değişkenle ingilizce karakterle yazılmalı
#4Özel kelimeler kullanmıyoruz
"""
isim = "furkan"
print(isim)

yas = 15
print(yas)

takim = input("tuttuğunuz takım nedir?")
print("tuttuğunuz takım = " + takim)

kdv = 0.30
print("defter:" , 50*kdv)
print("kalem:" , 50*kdv)
print("kitap:" , 50*kdv)
print("silgi:" , 50*kdv)
print("kalemtraş:" , 50*kdv)
print("laptop:" , 50*kdv)




kenar = int(input("kenar uzunluğu giriniz"))
print("a kişisinin çit ihtiyacı:" , kenar*1)
print("b kişisinin çit ihtiyacı:" , kenar*2)
print("c kişisinin çit ihtiyacı:" , kenar*3)
print("d kişisinin çit ihtiyacı:" , kenar*4)

masraf = float(input("günlük tost ve çay masrafınızı giriniz:"))
print("günlük masrafınız" , masraf*1)
print("haftalık masrafınız" , masraf*7)
print("aylık masrafınız" , masraf*30)
print("yıllık masrafınız" , masraf*365)


km = 5
mesafe = int(input("eviniz ve işiniz arasındaki mesafe kaç km?:"))
print("günlük masrafınız:" , mesafe*km*2 , "tl")
print("haftalık masrafınız:" , mesafe*km*14 , "tl")


tavuksayisi = int(input("çiftliğinizdeki tavuk sayısını giriniz:"))
ineksayisi = int(input("çiftliğinizdeki inek sayısını giriniz:"))
print("Çiftliğinizdeki hayvanlarınızın toplam ayak sayısı=" , tavuksayisi*2+ineksayisi*4)


takim = input("tuttuğunuz takımı giriniz:")
g = int(input("tuttuğunuz takımın galibiyet sayısını giriniz:"))
b = int(input("tuttuğunuz takımın beraberlik sayısını giriniz:"))
m = int(input("tuttuğunuz takımın malubiyet sayısını giriniz:")) 
#print(f"tuttuğunuz takım{takim}")
print("tuttuğunuz takım {}".format(takim))
print("galibiyetiniz {} beraberliğiniz {} malubiyetiniz {}".format(g,b,m))
print(takim ,"takımının toplam puanı=" , g * 3 + b * 1)
print(takim ,"takımının toplam yaptığı maç sayısı=" , g + b + m)
"""

araba = input("arabanız nedir?:")
model = input("arabanız modeli nedir?:")
km = input("arabanız kaç km?:")
print("arabanız {} arabanızın modeli {} arabanızın km`si {}".format(araba,model,km))