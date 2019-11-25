"""
Nama     : Ivan Arsyaditya
NIM      : A11.2019.12387
Kelompok : A11.4118
Tanggal  : 11-11-2019

"""
print("========================================")
print("Variabel Loop 1")
print("========================================")
a=1
while a<51 :
    print(a, end=" ")
    a+=1
print("\n")
print("========================================")
print("Variabel Loop 2")
print("========================================")
b=50
while b>0 :
    print(b, end=" ")
    b-=1
print("\n")
print("========================================")
print("Variabel Loop 3")
print("========================================")
a=1
b=50
while a<51 or b>0 :
    print(a, end=" ")
    print(b, end=" ")
    print(abs(a-b), end=" ")
    a+=1
    b-=1
