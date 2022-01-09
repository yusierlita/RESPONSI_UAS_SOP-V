print("RESPONSI SOP - V")
print("5200411094 - Yusi Erlita")
print("________________________")
print("SOAL NO. 1")

RAM = int(input("Masukkan Kapasitas Total RAM   ="))
Petabit = int(input("Masukkan Total Petabit     ="))
OS = int(input("Masukkan Kapasitas RAM Sistem Operasi   ="))
RAMsatu = int(input("Masukkan Kapasitas RAM Program 1   ="))
RAMdua = int(input("Masukkan Kapasitas RAM Program 2    ="))

KPetabit = RAM / Petabit
TotalRAM = OS + RAMsatu + RAMdua
RamTidakTerpakai = RAM - TotalRAM
JBlokSatu = RAM / Petabit
JBlokNol = RAM - KPetabit
print ("_________________________________")

print ("Total RAM                       =",RAM)
print ("Total Petabit                   =",Petabit)
print ("Kapasitas Per Petabit           =",KPetabit)
print ("Total RAM Yang Terpakai         =",TotalRAM)
print ("Total RAM Yang Tidak Terpakai   =",RamTidakTerpakai)
print ("Jumlah Blok Yang Bernilai 1     =",JBlokSatu)
print ("Jumlah Blok Yang Bernilai 0     =",JBlokNol)