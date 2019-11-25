import random
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


