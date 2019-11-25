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