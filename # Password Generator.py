# Password Generator
import random 
import string

harfler = string.ascii_letters
# print(harfler)

rakamlar = string.digits
# print(rakamlar)

ozeller = string.punctuation
# print(ozeller)

length = int(input("sifre uzunlugunu giriniz:"))
kalan = length % 3
parcalar = length // 3
harfsayisi = parcalar + kalan

rharf = random.choices(harfler, k=harfsayisi)
rrakam = random.choices(rakamlar, k=parcalar)
rozel = random.choices(ozeller, k=parcalar)
result = rharf + rrakam + rozel

random.shuffle(result)
print(result)