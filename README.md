# clis-filler (CLIS Data Filler)

Script ini dapat digunakan untuk mengisi data ke CLIS dengan mudah dari file CSV. bump

## Kebutuhan ENV

- pandas
- selenium webdriver
- argparse

Jika Anda menggunakan Anaconda, silakan install library tersebut lewat Anaconda Navigator > Environments. Jika menggunakan pip, install melalui:

`pip install selenium pandas argparse`

## Format CSV

1. CSV harus memiliki header/kolom pada baris pertama.
2. Pemisah kolom adalah koma ( , ).
3. Pemisah baris adalah CRLF.
4. Pemisah desimal adalah titik ( . ).
5. Kolom yang harus ada: npm, nama, nilai.
6. Urutan kolom harus sesuai.

Cara membuat file CSV yang benar:
1. Buka Microsoft Excel.
2. Buat 3 kolom: npm, nama, nilai.
3. Copy-paste data dari rekap ke sheet baru.
4. Save as sebagai *CSV (comma-separated)*.
5. Buka file CSV dengan Notepad, cek apakah sudah sesuai dengan ketentuan (pemisah, tanda koma, dll.).


## Cara Penggunaan clis.py

Semua perintah CLIS dieksekusi dari file clis.py

`python clis.py <mode> <file CSV> -u <username> -p <password> -c <kelas> -y <tahun masuk> -cid <kode kelas>`

Keterangan command line:

- **mode**, mode input data (master, los, nilai)
- **file CSV**, nama file CSV yang akan diinputkan.
- **-u**, username CLIS.
- **-p**, password CLIS, jika argumen ini dihilangkan, maka password akan sama dengan username CLIS.
- **-c**, kelas mahasiswa yang akan diinputkan (hanya berlaku pada mode **master**).
- **-y**, tahun mahasiswa yang akan diinputkan (hanya berlaku pada mode **master**).
- **-cid**, kode kelas mahasiswa yang akan diinputkan (hanya berlaku pada mode **los** dan **nilai**).

### Input Master Data -> Student List (mode: master)

Sintaks:

`python clis.py master <file CSV> -u <username> -p <password> -c <kelas> -y <tahun masuk>`

**Contoh:**

Input data master siswa
1. File input *kelas_a.csv*
2. Username & password CLIS: 065118116
3. Kelas: A
4. Tahun masuk: 2019

`python clis.py master kelas_a.csv -u 065118116 -c A -y 2019`

### Input Master Assistant -> List of Students (mode: los)

Sintaks:

`python clis.py los <file CSV> -u <username> -p <password> -cid <kode kelas>`

**Contoh:**

Input data siswa ke list of student
1. File input *kelas_a.csv*
2. Username & password CLIS: 065118116
3. Kode kelas: a6990ed96e2c5acac92acdcc3f83ba4e2893ad76 (lihat caranya di bawah)

`python clis.py los kelas_a.csv -u 065118116 -cid a6990ed96e2c5acac92acdcc3f83ba4e2893ad76`

### Input Scoring -> Final Test (mode: nilai)

Sintaks:

`python clis.py nilai <file CSV> -u <username> -p <password> -cid <kode kelas>`

**Contoh:**

Input nilai akhir siswa
1. File input *kelas_a.csv*
2. Username & password CLIS: 065118116
3. Kode kelas: a6990ed96e2c5acac92acdcc3f83ba4e2893ad76 (lihat caranya di bawah)

`python clis.py nilai kelas_a.csv -u 065118116 -cid a6990ed96e2c5acac92acdcc3f83ba4e2893ad76`

### Cara Mengetahui ID Kelas

1. Anda sudah harus membuat kelas dari menu Master Assitant > Lecture List
2. Buka menu Master Asistant > List of Students
3. Klik tombol *oranye* kemudian periksa link nya. Yang di bold itu adalah ID kelas-nya.

    http://labkom.ilkom.unpak.ac.id/?m=master&p=form_list_student&id=**a6990ed96e2c5acac92acdcc3f83ba4e2893ad76**