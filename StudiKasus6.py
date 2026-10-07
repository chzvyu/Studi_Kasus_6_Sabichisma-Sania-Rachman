import json

with open("nilai.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def tampilkan_data():
    print("=== DATA NILAI MAHASISWA ===")

    if data == []:
        print("Belum ada data nilai.")
    else:
        for mahasiswa in data:
            print("NIM   :", mahasiswa["nim"])
            print("Nama  :", mahasiswa["nama"])
            print("Nilai :", mahasiswa["nilai"])
            print("----------------------")


def tambah_data():
    nim = input("Masukkan NIM   : ")
    nama = input("Masukkan Nama  : ")
    nilai = input("Masukkan Nilai : ")

    data_baru = {
        "nim": nim,
        "nama": nama,
        "nilai": nilai
    }

    data.append(data_baru)

    with open("nilai.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Data nilai berhasil ditambahkan!")


def main():
    while True:
        print("=== SISTEM PENCATATAN NILAI MAHASISWA ===")
        print("1. Tampilkan Data")
        print("2. Tambah Data Nilai")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_data()

        elif pilihan == "2":
            tambah_data()

        elif pilihan == "3":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia!")


main()