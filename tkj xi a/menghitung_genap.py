batas = int(input("MAsukkan Batas Angka: "))
jumlah_genap = 0

for angka in range (1, batas+1):
    if angka % 2 == 0:
        jumlah_genap += 1

print("Jumlah angka genap dalam rentang 1 hingga", batas, "adalah: ", jumlah_genap )        