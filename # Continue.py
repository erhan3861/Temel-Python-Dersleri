# Continue
sayi = int(input("sayı giriniz:"))
i = 0
while i < sayi:
  i += 1
  if i > 10 and i < 20:
    continue
  print(i)