"""
Nama     : Ivan Arsyaditya
NIM      : A11.2019.12387
Kelompok : A11.4118
Tanggal  : 11-11-2019

"""
import os, sys, random
def main() :
    soal1a()
    soal1b()
    soal1c()
    soal2()
    soal3()
print("====================================================")
x=int(input("Masukkan Angka Pembuat Pola : "))
print("====================================================")
def soal1a() :
    a=1
    baris = 1
    while baris <= x :
        kolom = 1
        while kolom <= x :
            if baris==kolom :
                print(a, end=" ")
                a+=1
                kolom+=1
            elif kolom <= baris :
                print(a,end=" ")
                a+=1
                kolom+=1
            else :
                print(" ", end=" ")
                kolom+=1
        baris+=1
        print("")
    print("====================================================")
def soal1b() :
    baris=1
    a=1
    while baris <= x :
        kolom=1
        while kolom<= x :
            if baris==kolom :
                print(a, end=(" "))
            elif baris+kolom==6 :
                print(a, end=(" "))
            else :
                print(" ",end=(" "))
            kolom+=1
        a+=1
        baris+=1
        print("")
    print("====================================================")
def soal1c() :
    baris = 1
    a=00
    b=10
    while baris <= x :
        kolom=1
        c=0
        while kolom <= x :
            if baris%2 != 0 :
                a=baris
                print("0{}".format(a), end=(" "))
            elif baris%2 == 0 :
                c+=1
                print(b+c, end=(" "))
            else :
                break
            kolom+=1
        b+=10
        baris+=1
        print("")
    print("====================================================")
def soal2() :
    x=int(input("Masukkan Minggu Perhitungan = "))
    total=0
    minggu=1
    while x >= 1 :
        y=7
        print("Minggu ke-{} = ".format(minggu))
        makan=45000
        hari=1
        while y >= 1 :
            print("Hari ke-{} = {}".format(hari, makan))
            total+=makan
            makan-=1000
            y-=1
            hari+=1
        print("Pengeluaran Total = {}".format(total))
        minggu+=1
        x-=1
def soal3() :
    a=4
    point=0
    x=random.randint(1,50)
    while a >= 0 :
        print("=========================")
        b=int(input("Masukkan Angka Tebakkan = "))
        print("=========================")
        if b == x :
            print("Selamat Anda Berhasil Menebak Angka : {}".format(x))
            point+=1
            print("Jumlah Point Anda : {}".format(point))
            x=random.randint(1,50)
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

if __name__ == "__main__":
    main()