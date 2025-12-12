# start,end,step
# for i in range(0,100,6):
#     print(i)

# girdi = input("karakter yazınız")
# abc[as[asdf[.124
# for i in range(len(girdi)):
#     if girdi[i] == "[":
#         print(f"sıra numarası ={i}")

girdi = input("kelime giriniz").lower()
sesli = "aeiouıüö"
for i in range(len(girdi)):
    if girdi[i] in sesli:
        print(f"sesli harf={i}")