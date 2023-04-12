Nama : ["Ali", "Budi", "Caca", "Dodo", "Elo"]
Nim : ["Ti001", "Ti002", "Ti003", "Ti004", "Ti005"]
Fisika : ["80", "70", "75", "85", "90"]
Biologi : ["81", "73", "72", "81", "91"]
Matematika : ["89", "71", "73", "86", "92"]

Nilai = (Fisika + Biologi + Matematika)/3
A = 4
B = 3
C = 2
D = 1
E = 0

if Nilai >= 80:
    Nilai : A
elif Nilai >= 70:
    Nilai : B
elif Nilai >= 60:
    Nilai : C
elif Nilai >= 50:
    Nilai : D
else:
    Nilai : E

print(Nama, "IPK", Nilai)