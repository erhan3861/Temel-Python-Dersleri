# Sonsuz Döngü Ve Random
import random


# yazı tura
"""
while True:
  result = random.randint(1,2)
  user =  int(input("yazı için 1 tura için 2 giriniz"))
  if result == user:
    print("bildiniz")
  else:
    print("bilemediniz")
"""

# zar oyunu
"""
while True:
  result = random.randint(1,6)
  user =  int(input("zardan bir sayı seçiniz"))
  if result == user:
    print("bildiniz")
  else:
    print("bilemediniz bilgisayar =" ,result)
"""

# taş kağıt makas
"""
secenekler = "tkm"
while True:
  result = random.choice(secenekler)
  user = input("taş/t kağıt/k makas/m")
  
  
  if user not in secenekler:
    print("doğru seçenek giriniz")
  elif user == result:
    print("berabere")
  elif user == "t" and result == "m":
    print("kazandınız")
  elif user == "k" and result == "t":
    print("kazandınız")
  elif user == "m" and result == "k":
    print("kazandınız")
  else:
    print("kaybettiniz")
"""

# penaltı oyunu
"""
kale = "123"
puan = 0
kalecipuan = 0
while puan < 3 and kalecipuan < 3:
  result = random.choice(kale)
  user = input("nereye şut atıcaksınız sol:1 orta:2 sağ:3")
  if user not in kale:
    print("doğru seçenek giriniz")
  elif user == result:
    print("kaleci topu tuttu")
    kalecipuan += 1
  else:
    puan += 1
    print("gol attınız")
if puan == 3:
  print("kazandınız")
else:
  print("kaybettiniz")
"""

# penaltı oyunu 2
"""
kale = "123"
puan = 0
kalecipuan = 0
while True:
  result = random.choice(kale)
  user = input("nereye şut atıcaksınız sol:1 orta:2 sağ:3")
  if user not in kale:
    print("doğru seçenek giriniz")
  elif user == result:
    print("kaleci topu tuttu")
    kalecipuan += 1
  else:
    puan += 1
    print("gol attınız") 
  if puan == 3 or kalecipuan == 3:
    break
if puan == 3:
  print("kazandınız")
else:
  print("kaybettiniz")
"""

while True:
  number = random.randint(1,10)
  print(number)
  if number == 1:
    break