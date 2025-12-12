# stringler
"""
print("f" in "furkan")
print("j" not in "furkan")


mail = input("mail adresi giriniz")
if "@" in mail[0]:
  print("invalid")
elif ".com" not in mail[-4:]:
  print("invalid")
elif "@" not in mail:
  print("invalid")
else:
  print("valid")
"""
"""
name = "furkan"
# name[0] = "b"
name = "b" + name[1:]
print(name)
print(name[::-1])
"""

# palindrom sorusu
"""
kelime = input("kelime giriniz")
if kelime == kelime[::-1]:
  print("kelime palindromdur")
else:
  print("kelime palindrom değildir")
"""

# stringlerin methodları
"""
print("furkan".islower())
print("FURKAN".isupper())
print("furKan".islower())
"""
kelime = input("kelime giriniz")
if kelime[0].isupper() and kelime[1:].islower():
  print("kelime başlıktır")
else:
  print("kelime başlık değildir")