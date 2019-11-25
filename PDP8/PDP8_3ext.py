import os, sys, random
point=0
print("=========================")
print("\tWELCOME TO")
print("     GUESS THE NUMBER")
print("\t  GAME\t\t")
print("=========================")
print("Choose Difficulty")
print("=========================")
print("1.Easy")
print("2.Medium")
print("3.Hard")
print("4.Dewa Judi")
print("5.Dukun")
print("=========================")
dif=input("Pilih Difficulty(1-5) = ")
if dif == "1" :
    x=random.randint(1,10)
    a=9
    print("Difficulty Easy range angka = 1-10 sama nyawa = 10")
elif dif == "2" :
    x=random.randint(1,50)
    a=9
    print("Difficulty Medium range angka = 1-50 sama nyawa = 10")
elif dif == "3" :
    x=random.randint(1,50)
    a=4
    print("Difficulty Hard range angka = 1-10 sama nyawa = 5")
elif dif == "4" :
    x=random.randint(1,1000)
    a=9
    print("Difficulty Dewa Judi range angka = 1-1000 sama nyawa = 10")
elif dif == "5" :
    x=random.randint(1,1000)
    a=2
    print("Difficulty Dukun range angka = 1-1000 sama nyawa = 3")
else :
    print("Error!!Choose 1-5")
while a >= 0 :
    print("=========================")
    b=int(input("Masukkan Angka Tebakkan = "))
    print("=========================")
    if b == x :
        print("Selamat Anda Berhasil Menebak Angka : {}".format(x))
        point+=1
        print("Jumlah Point Anda : {}".format(point))
        if dif == "1" :
            x=random.randint(1,10)
        elif dif == "2" :
            x=random.randint(1,50)
        elif dif == "3" :
            x=random.randint(1,50)
        elif dif == "4" :
            x=random.randint(1,1000)
        elif dif == "5" :
            x=random.randint(1,1000)
        else :
            break
    elif b < x :
        print("Angka Tebakan Lebih Kecil")
        print("Nyawa Anda Masih {}".format(a))
        a-=1
    elif b > x :
        print("Angka Tebakan Lebih Besar")
        print("Nyawa Anda Masih {}".format(a))
        a-=1
    else :
        break
print("=========================")
print("Nyawa Anda Habis!!Anda gagal menebak angka: {}".format(x))
print("Jumlah Point anda : {}".format(point))
print("=========================")


