#progres matriks 3 x 3

matriksA = [[1,2,3],
            [5,6,7],
            [8,9,10]]
matriksB = [[11,12,13],
            [14,15,16],
            [17,18,19]]
print("-"*55)
print(matriksA)
print("bentuk kedua kotak matriks sebagai berikut: ")
#memanggil anggota untuk baris
for x in range(0, len(matriksA)):
#mengatur matriks ke bawah
    print()
#memanggil anggota untuk kolom
    for y in range(0,len(matriksA[0])):
#memanggil anggota mengatur jarak antar anggota ke kanan
        print(matriksA[x][y], end=" "),
    print()
print("-"*55)

print("-"*55)
#proses penjumlahan matrik 1 dan matrik 2

for x in range(0,len(matriksA)):
    #print()
    for y in range(0,len(matriksA[0])):
        print(matriksA[x][y]-matriksB[x][y], end=" ")

print()