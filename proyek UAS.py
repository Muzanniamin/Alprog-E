
# Program unik menampilkan informasi mahasiswa dengan variabel, input, dan operasi logika/aritimatika

# Menampilkan nama dan NIM
print("Nama: Muzanni Amin, M Hafzan Wazani, Denis Eka Gunanda, Nabel Alawi, Mufrizahy Jordan Aslam")
print("NIM: 24241155, 24241168, 24241172, 24241160, 24241167")

# Meminta input dari user
nim_input = int(input("Masukkan NIM Anda: "))

# Daftar NIM dan nama
nim_nama = {
    24241155: "Muzanni Amin",
    24241168: "M Hafzan Wazani",
    24241172: "Denis Eka Gunanda",
    24241160: "Nabel Alawi",
    24241167: "Mufrizahy Jordan Aslam"
}

# Cek NIM
nama = nim_nama.get(nim_input, "NIM tidak ditemukan dalam daftar")
print(f"Nama Anda: {nama}")

# Operasi aritmatika
angka1 = 8
angka2 = 3
hasil_penambahan = angka1 + angka2
hasil_pengurangan = angka1 - angka2
hasil_perkalian = angka1 * angka2
hasil_pembagian = angka1 / angka2

print(f"Hasil Penambahan: {hasil_penambahan}")
print(f"Hasil Pengurangan: {hasil_pengurangan}")
print(f"Hasil Perkalian: {hasil_perkalian}")
print(f"Hasil Pembagian: {hasil_pembagian}")

# Operasi logika (and, or, xor)
x = True
y = True

print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"{x} xor {y}: {x != y}")
