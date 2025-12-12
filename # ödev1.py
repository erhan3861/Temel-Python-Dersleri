# ödev1

# ödev1 basketbolda kullanıcıdan basket attığı mesafe,buna göre kaç puan aldığı
# ödev2 bir takımın attığı ve yediği goller buna göre avaraj
# ödev3 bir sporcunun günlük antreman yaptığı süre(dakika) haftalık antreman yaptığı saat
# ödev4 bir öğrencinin okula giderken geçirdiği zaman (dakika) geçen zamanı saat olarak ver
# ödev5 bir öğrencinin hafta içi ve hafta sonu yaptığı spor saati aylık sporda geçirdiği zaman(gün)

# 1



# 2
"""
takim = input("Takım giriniz:")
ygol = int(input(takim + " takımının yediği gol sayısını giriniz:"))
agol = int(input(takim + " takımının attığı gol sayısını giriniz:"))
print("Takımın avarajı=" , agol - ygol)
"""

# 3
"""
antremans = int(input("günlük spor yaptığınız süreyi dakika olarak giriniz:"))
print("Haftalık spor süreniz=" , antremans*7/60 , "saat,dir")
"""

# 4
"""
yol = int(input("Okula kaç dakikada gidiyorsun?:"))
print("Bu değer " , yol/60 , "saate eşittir")
"""

#5
"""
haftaici = int(input("Hafta içi kaç saat spor yapıyorsun?:"))
haftasonu = int(input("Hafta sonu kaç saat spor yapıyorsun?:"))
print("Ayda gün olarak yaptığınız toplam spor:" , haftasonu*4+haftaici*4 , "gündür")
"""