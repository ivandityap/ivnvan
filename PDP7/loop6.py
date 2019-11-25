"""
Nama     : Ivan Arsyaditya
NIM      : A11.2019.12387
Kelompok : A11.4118
Tanggal  : 11-11-2019

"""
print("=====================================")
print("Menggunakan While")
print("=====================================")
a = 0
b = 127
while a<=b :
    asc=str(chr(a))
    print(asc, end=" ")
    a+=1
print("\n")
print("=====================================")
print("Menggunakan for")
print("=====================================")
for x in range(128) :
    asc=str(chr(x))
    print(asc, end=" ")
print("\n")
print("=====================================")
print("Menggunakan do-while")
print("=====================================")
a=0
b=127
while True :
    asc=str(chr(a))
    print(asc, end=" ")
    a+=1
    if a>127 :
        break


