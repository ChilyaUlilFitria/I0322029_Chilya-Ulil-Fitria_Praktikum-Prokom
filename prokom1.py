#input deklarasi database

kelas = ["Ali", "Budi", "Ana", "Caca"]


print("-"*55)
#output
print(kelas[1])

print("-"*55)

#proses

for i in range(0,len(kelas)):
#output yang berulang
    print("nama mahasiswa ke ", i, " adalah = ", kelas[i])

print("-"*55)

#menambah database
kelas.append("Ade")
kelas.insert(2,"Kaka")
kelas.remove("Ali")

for i in range(0,len(kelas)):
#output yang berulang
    print("nama mahasswa ke ", i, "adalah= ", kelas[i])