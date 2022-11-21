data = []

while True:
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    akhir = float(tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
    data.append ([nama, nim, tugas, uts, uas, int(akhir)])
    lagi = input ("Tambah lagi (y/t)?")
    if lagi.lower() =="t":
        break

print("\n                               Daftar Nilai Mahasiswa")
print("============================================================================")
print("| No |  Nama         |  NIM  |  Tugas  |  UTS  |  UAS  |  Akhir  |")
print("============================================================================")
i = 0
for nilai in data:
    i += 1
    print("|  {no:2d}  |  {nama:12s}  |  {nim:9s}  |  {tugas:5d}  |  {uts:5d}  |  {uas:5d}  |  {akhir:6.2f}  |" .format(no=i, nama=nilai[0], nim=nilai[1], tugas=nilai[2], uts=nilai[3], uas=nilai[4], akhir=nilai[5]))

print("===========================================================================")