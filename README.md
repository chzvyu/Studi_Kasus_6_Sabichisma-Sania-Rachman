# Studi_Kasus_6_Sabichisma-Sania-Rachman
Nama : Sabichisma Sania Rachman <br>
NIM : 013 <br>
Sistem Pencatatan Nilai Mahasiswa (NIM Ganjil) <br>

 Penjelasan kode: <br>
  1. import json digunakan untuk menggunakan library JSON dalam Python.
  2. open("nilai.json", ...) → membuka file nilai.json.
  3. "r" merupakan mode read, yaitu membaca file.
  4. encoding="utf-8" untuk menentukan format karakter agar teks dapat dibaca dengan baik.
  5. as f yaitu file yang dibuka disimpan sementara dalam variabel f.
  6. json.load(f) untuk membaca isi file JSON dan mengubahnya menjadi data Python.
  7. data untuk menyimpan seluruh data mahasiswa yang berasal dari file JSON.
  8. def merupakan function yang digunakan untuk menampilkan data dan menambahkan data.
  9. data.append(data_baru) untuk menambahkan data baru ke list data. <br>
 
Output program: <br>
  1. Jika memilih pilihan 1 yaitu tampilkan data namun list data masih kosong. <br>
     <img width="410" height="224" alt="Screenshot 2026-10-07 214052" src="https://github.com/user-attachments/assets/e2ef50d0-d33b-467e-b5e8-a3e6aa69f149" /> <br>
  2. Jika memilih pilihan 2 yaitu menambahkan data, maka kita akan diminta input data berupa nim, nama, dan nilai. <br>
     <img width="415" height="244" alt="Screenshot 2026-10-07 214111" src="https://github.com/user-attachments/assets/3ea0cfcb-e144-451a-997e-1f2a4b438cae" /> <br>
  3. Tambahkan data lagi. <br>
     <img width="396" height="251" alt="Screenshot 2026-10-07 214136" src="https://github.com/user-attachments/assets/606f13fc-a7b4-49e1-a32b-5fc2cd8b5742" /> <br>
  4. Jika kita memilih pilihan 1 yaitu menampilkan data setelah menambahkan data. <br>
     <img width="421" height="358" alt="Screenshot 2026-10-07 214151" src="https://github.com/user-attachments/assets/96e7b17c-00d6-450b-8e00-8dbd8fa03e7d" /> <br>
  5. Jika memilih pilihan 3 yaitu keluar, maka program selesai. <br>
     <img width="467" height="183" alt="Screenshot 2026-10-07 214213" src="https://github.com/user-attachments/assets/6a20db10-15f8-41d4-9057-f1d577e18421" /> <br>
     6. Jika program di run kembali maka data tetap tersimpan. <br>
        <img width="456" height="378" alt="Screenshot 2026-10-07 215538" src="https://github.com/user-attachments/assets/8c3123e3-88c2-4985-af68-996902ca5056" /> <br> <img width="395" height="361" alt="Screenshot 2026-10-07 220445" src="https://github.com/user-attachments/assets/5a885101-4fef-48d4-9d33-0163e08715d3" /> <br>






