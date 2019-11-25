"""
Nama     : Ivan Arsyaditya
NIM      : A11.2019.12387
Kelompok : A11.4118
Tanggal  : 11-11-2019

"""

harga_3_ayam = 150000
umur_ayam = 3
telur = 0
usia_produktif_ayam = 17
hari = 30
telur_per_hari = 3
keuntungan = 0
harga_per_kilogram = 14500
perawatan = 200000
total_lama_perawatan = 18

print ("=========================================")

#Jumlah Telur
for i in range(usia_produktif_ayam) :
    umur_ayam += 1
    telur = telur+(telur_per_hari*hari)
    print ("Jumlah Telur Bulan Ke - {} = {}".format(umur_ayam,telur))
print ("=========================================")

# Print Jumlah Telur
print ("Jumlah Total Butir Telur = {} KG".format(telur))

#Keuntungan
keuntungan = (telur*harga_per_kilogram)-(perawatan*total_lama_perawatan)-harga_3_ayam
print ("Total Keuntungan Penjualan Yaitu = Rp.{} ".format(keuntungan))


