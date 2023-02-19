book1 = {
    "Nama Koleksi Buku": "Romeo and Juliet",
    "Nama Pengarang Buku": "William Shakespeare",
    "Tahun Terbit": 1597,
    "Stock": 3
}
book2 = {
    "Nama Koleksi Buku": "Soekarno: Arsitek Bangsa",
    "Nama Pengarang Buku": "Bob Hering      ",
    "Tahun Terbit": 2012,
    "Stock": 5
}
book3 = {
    "Nama Koleksi Buku": "The Lord of The Rings",
    "Nama Pengarang Buku": "J.R.R. Tolkien",
    "Tahun Terbit": 1954,
    "Stock": 4
}
listBuku = { 
    "book1": book1,
    "book2": book2,
    "book3": book3
}

keranjangPinjam = {}

def koleksiBuku():
    print('\nKoleksi Buku\n')
    print(f"{'Index':<6} {'| Nama Koleksi Buku':<30} {'| Nama Pengarang Buku':<25} {'| Tahun Terbit':<13} {'| Stock':<5}")
    for buku in listBuku.keys() :
        Index = buku
        Nama = listBuku[buku]["Nama Koleksi Buku"]
        Pengarang = listBuku[buku]["Nama Pengarang Buku"]
        Tahun = listBuku[buku]["Tahun Terbit"]
        Stock = listBuku[buku]["Stock"]
        print(f"{Index:<8} {Nama:<30} {Pengarang:<25} {Tahun:<14} {Stock:<5}")

while(True) :
    pilihanMenu = input('''\n
    Selamat Datang di Perpustakaan Guna Jaya

    Daftar Pilihan Menu :
    1. Tampilkan Koleksi Buku
    2. Menambah Koleksi Buku
    3. Update Data Koleksi Buku
    4. Menghapus Koleksi Buku
    5. Meminjam Koleksi Buku
    6. Exit Program

    Silahkan Memasukkan Angka Pilihan Menu Anda : ''')

    if(pilihanMenu == '1') :
        menuHalaman1 = input('''\n
        Apa Koleksi Buku Yang Sedang Anda Cari?

        Daftar Pilihan Menu :
        1. Tampilkan Seluruh Koleksi
        2. Cari Koleksi Buku Berdasarkan Index
        3. Exit

        Silahkan Memasukkan Angka Pilihan Menu Anda : ''')

        if(menuHalaman1 == '1') :
            koleksiBuku()
        elif(menuHalaman1 == '2') :
            while(True):
                cariBuku = input('\nSilahkan Memasukkan Kode Index Buku Yang Ingin Dicari : ')
                if cariBuku in listBuku.keys() :
                    print('\nHasil Pencarian Koleksi Buku Berdasarkan Index\n')
                    print(f"{'Index':<6} {'| Nama Koleksi Buku':<30} {'| Nama Pengarang Buku':<25} {'| Tahun Terbit':<13} {'| Stock':<5}")
                    Index = cariBuku
                    Nama = listBuku[cariBuku]["Nama Koleksi Buku"]
                    Pengarang = listBuku[cariBuku]["Nama Pengarang Buku"]
                    Tahun = listBuku[cariBuku]["Tahun Terbit"]
                    Stock = listBuku[cariBuku]["Stock"]
                    print(f"{Index:<8} {Nama:<30} {Pengarang:<25} {Tahun:^14} {Stock:^5}")
                    cariLagi = input('\nApakah Ada Lagi Koleksi Buku Yang Ingin Dicari? (YES/NO): ')
                    if cariLagi == 'NO':
                        break
                else :
                    print('\n~ Tidak Ada Koleksi Buku Dengan Kode Index Tersebut ~')
                    continue
        else :
            continue
    
    elif(pilihanMenu == '2') :
        
        while(True):
            koleksiBuku()
            print('\nMenambah Koleksi Buku')
            for buku in listBuku.keys() :
                Index = buku
            bookTemplate = {
             "Nama Koleksi Buku": "namabuku",
             "Nama Pengarang Buku": "namapengarang",
             "Tahun Terbit": 0000,
             "Stock": 0
            }
            bukuBaru = dict.fromkeys(bookTemplate.keys())
            indexBaru = input('\nSilahkan Masukkan Index Koleksi Buku : ')
            if indexBaru in listBuku.keys() :
                print('\n~ Kode Index Untuk Koleksi Buku Tersebut Sudah Ada ~')
                continue
            bukuBaru["Nama Koleksi Buku"] = input('Silahkan Masukkan Judul Buku : ')
            bukuBaru["Nama Pengarang Buku"] = input('Silahkan Masukkan Nama Pengarang Buku : ')
            while(True):
                bukuBaru["Tahun Terbit"] = int(input('Silahkan Masukkan Tahun Terbit Buku : '))
                if (bukuBaru["Tahun Terbit"] > 2023):
                    print('~ Silahkan Masukkan Tahun Terbit Yang Benar ~')
                else :
                    break
            bukuBaru["Stock"] = int(input('Silahkan Masukkan Jumlah Stock Buku : '))
            simpanData = input('Simpan Data Koleksi Buku Terbaru? (YES/NO): ')
            if(simpanData == 'NO'):
                print('\n~ Data Koleksi Buku Baru Batal Tersimpan ~')
                break  
            elif simpanData == 'YES':
                listBuku.update({indexBaru: bukuBaru})
                koleksiBuku()
                print('\n')
                tambahLagi = input('~ Data Koleksi Buku Baru Telah Tersimpan ~\nApakah Anda Mau Menambahkan Koleksi Buku Lain? (YES/NO): ')
                if tambahLagi == 'YES':
                    continue
                elif(tambahLagi == 'NO'):
                    break

    elif(pilihanMenu == '3') :
        print('\nUpdate Data Koleksi Buku')
        while(True):
            updateBuku = input('\nSilahkan Masukkan Kode Index Koleksi Buku Yang Ingin Di-Update : ')
            if updateBuku not in listBuku:
                print('\n~ Tidak Ada Buku Dengan Kode Index Tersebut di Koleksi ~')
                continue
            else :
                print('\nPilihan Koleksi Buku Yang Akan Di-Update\n')
                print(f"{'Index':<6} {'| Nama Koleksi Buku':<30} {'| Nama Pengarang Buku':<25} {'| Tahun Terbit':<13} {'| Stock':<5}")
                Index = updateBuku
                Nama = listBuku[updateBuku]["Nama Koleksi Buku"]
                Pengarang = listBuku[updateBuku]["Nama Pengarang Buku"]
                Tahun = listBuku[updateBuku]["Tahun Terbit"]
                Stock = listBuku[updateBuku]["Stock"]
                print(f"{Index:<8} {Nama:<30} {Pengarang:<25} {Tahun:^14} {Stock:^5}")
                break
        keysUpdate = input('\nSilahkan Masukkan Nama Kolom Data Yang Ingin Di-Update: ')
        listBuku[updateBuku][keysUpdate] = input('\nSilahkan Masukkan Update Data Terbaru: ')
        koleksiBuku()
        print(f"\n~ Data Koleksi Buku Dengan Kode Index: {updateBuku} Sudah Berhasil Di-Update ~")

    elif(pilihanMenu == '4') :
        while(True):
            koleksiBuku()
            indexBuku = input('\nSilahkan Masukkan Kode Index Koleksi Buku Yang Ingin Dihapus : ')
            if indexBuku not in listBuku:
                print('\n~ Tidak Ada Buku Dengan Kode Index Tersebut di Koleksi ~')
                continue
            else :
                break
        yakinHapus = input('\nApakah Anda Yakin Mau Menghapus Koleksi Buku Ini? (YES/NO): ')
        if(yakinHapus == 'NO'):
            print(f"\n~ Buku Dengan Kode Index {indexBuku} Tidak Berhasil Dihapus ~ ")
            continue
        elif(yakinHapus == 'YES'): 
            listBuku.pop(indexBuku)
            koleksiBuku()
            print(f"\n~ Buku Dengan Kode Index: {indexBuku} Sudah Berhasil Dihapus ~")
        else :
            continue

    elif(pilihanMenu == '5') :

        while(True):
            koleksiBuku()
            for item in keranjangPinjam.keys() :
                indexPinjam = item
            pinjamTemplate = {
                "Nama Koleksi Buku": "namabuku",
                "Tahun Terbit": 0000,
                "Quantity": 0,
                "Masa Pinjam": 0
                }
            while(True):
                pinjamBuku = dict.fromkeys(pinjamTemplate.keys())
                indexPinjam = input('\nSilahkan Masukkan Index Buku Yang Akan Dipinjam : ')
                if indexPinjam not in listBuku.keys() :
                    print('\n~ Tidak Ada Kode Index Buku Tersebut di Perpustakaan Guna Jaya, Silahkan Pilih Buku Lain! ~')
                    continue
                else:
                    break
            pinjamBuku["Nama Koleksi Buku"] = listBuku[indexPinjam]["Nama Koleksi Buku"]
            pinjamBuku["Tahun Terbit"] = listBuku[indexPinjam]["Tahun Terbit"]
            while(True):
                pinjamBuku["Quantity"] = int(input('\nSilahkan Masukkan Jumlah Buku Yang Akan Dipinjam : '))    
                if(pinjamBuku["Quantity"] != 1) :
                    print('\n~ Hanya Diperbolehkan Untuk Meminjam 1 Judul Buku ~')
                    continue
                else :
                    break
            while(True):    
                pinjamBuku["Masa Pinjam"] = int(input('\nSilahkan Masukkan Masa Pinjam Buku (Hari) : '))
                if(pinjamBuku["Masa Pinjam"] > 14) :
                    print('\n~ Durasi Yang Diperbolehkan Untuk Meminjam Maksimal 14 Hari ~')
                    continue
                else :
                    break
            keranjangPinjam.update({indexPinjam: pinjamBuku})
            sisaStock = listBuku[indexPinjam]["Stock"] - 1
            listBuku[indexPinjam].update({"Stock":sisaStock})
            print('\nIsi Keranjang Pinjam :\n')
            print(f"{'Index':<6} {'| Nama Koleksi Buku':<30} {'| Tahun Terbit':^13} {'| Quantity':^5} {'| Masa Pinjam':^12}")
            print(f"{indexPinjam:<8} {keranjangPinjam[indexPinjam]['Nama Koleksi Buku']:<30} {keranjangPinjam[indexPinjam]['Tahun Terbit']:^14} {keranjangPinjam[indexPinjam]['Quantity']:^9} {keranjangPinjam[indexPinjam]['Masa Pinjam']:^12}")   
            checker = input('\nApakah Anda Mau Meminjam Buku Yang Lain? (YES/NO) : ')
            if(checker == 'YES'):
                continue 
            elif(checker == 'NO'):
                print('\nKoleksi Buku Yang Akan Dipinjam : \n')
                print(f"{'Index':<6} {'| Nama Koleksi Buku':<30} {'| Tahun Terbit':^13} {'| Quantity':^5} {'| Masa Pinjam':^12}")      
                for item in keranjangPinjam :
                    print(f"{item:<8} {keranjangPinjam[item]['Nama Koleksi Buku']:<30} {keranjangPinjam[item]['Tahun Terbit']:^14} {keranjangPinjam[item]['Quantity']:^9} {keranjangPinjam[item]['Masa Pinjam']:^12}")
                namaPeminjam = input('\nSilahkan Masukkan Nama Peminjam : ')
                while(True):
                    NIK_KTP = input('Silahkan Masukkan NIK KTP Anda : ')
                    if len(NIK_KTP) != 16:
                        print('~ NIK KTP Anda Salah, Silahkan Masukkan Kembali 16 Digit NIK KTP Anda ~')
                        continue
                    else : break
                tanggal = len(range(1,31))
                bulan = len(range(1,13))
                tahun = 2023
                while(True):
                    tanggalPinjam = int(input('Masukkan Tanggal Peminjaman : '))
                    if tanggalPinjam > tanggal:
                        print('~ Silahkan Masukkan Tanggal Peminjaman Yang Benar ~')
                        continue
                    else: break
                while(True):
                    bulanPinjam = int(input('Masukkan Bulan Peminjaman (In Number) : '))
                    if bulanPinjam > bulan:
                        print('~ Silahkan Masukkan Bulan Peminjaman Yang Benar ~')
                        continue
                    else : break
                while(True):
                    tahunPinjam = int(input('Masukkan tahun Peminjaman : '))
                    if tahunPinjam > tahun:
                        print('~ Silahkan Masukkan Tahun Peminjaman Yang Benar ~')
                        continue
                    else: break
                print('\nData Peminjam Koleksi Buku Perpustakaan Guna Jaya:')
                print(f"\n{'Nama Peminjam':<18} {'| NIK KTP':<19} {'| Nama Koleksi Buku':<28} {'| Quantity':^5} {'| Tanggal Meminjam':<19} {'| Masa Pinjam':^12}")
                for item in keranjangPinjam :
                    print(f"{namaPeminjam:<20} {NIK_KTP:<19} {keranjangPinjam[item]['Nama Koleksi Buku']:<28} {keranjangPinjam[item]['Quantity']:^10} {tanggalPinjam:>5}/{bulanPinjam:^3}/{tahunPinjam:^5} {keranjangPinjam[item]['Masa Pinjam']:^18}")
                for item in keranjangPinjam :
                    tanggalKembali = tanggalPinjam + keranjangPinjam[item]['Masa Pinjam']
                    bulanKembali = bulanPinjam
                    tahunKembali = tahunPinjam
                    lewatTanggal = tanggalKembali-30 
                    lewatBulan = bulanKembali+1
                    akhirTahun = lewatBulan-12
                    lewatTahun = tahunKembali+1
                    if tanggalKembali <= 30:
                        print(f"\n~ Silahkan Kembalikan Buku {keranjangPinjam[item]['Nama Koleksi Buku']} Paling Lambat Tanggal {tanggalKembali}/{bulanKembali}/{tahunKembali} ~")
                    elif tanggalKembali>30 and lewatBulan>12:
                        print(f"\n~ Silahkan Kembalikan Buku {keranjangPinjam[item]['Nama Koleksi Buku']} Paling Lambat Tanggal {lewatTanggal}/{akhirTahun}/{lewatTahun} ~")
                    elif tanggalKembali >30 :
                        print(f"\n~ Silahkan Kembalikan Buku {keranjangPinjam[item]['Nama Koleksi Buku']} Paling Lambat Tanggal {lewatTanggal}/{lewatBulan}/{tahunKembali} ~")    
                break

    elif(pilihanMenu == "6") :
        print('\n~ Anda Telah Berhasil Keluar Dari Program ~\n')
        break
