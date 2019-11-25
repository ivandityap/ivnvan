import os, sys
def main() :
    soal1a()
    soal1b()
    soal1c()
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
if __name__ == "__main__":
    main()