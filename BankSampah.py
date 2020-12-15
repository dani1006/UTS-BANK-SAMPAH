# sistem bank sampah 

nama = input("Siapa nama Anda: ")
alamat = input("Alamat: ")

def harga():
    berat_sampah = int(input("Berapa Kilo sampah anda? "))
    lama_gabung = input("apakah anda sudah bergabung selama lebih dari 5 bulan?[Y/T]")
    if lama_gabung == "y":
        harga_sampah_tambahan = berat_sampah * 5000
        print()
        print("Harga Sampah: ",harga_sampah_tambahan)
        print()
    else:
        harga_sampah = berat_sampah * 2500
        print()
        print("Harga sampah: ",harga_sampah)
        print()


pilihan = 1
while pilihan !=0:
    print()
    print("---Menu Bank Sampah---")
    print("1. Harga Sampah /KG")
    print("2. Ingin Stor ")
    print("0. exit")
    print()
    pilihan = int(input("Masukkan Nomor Menu: "))
    if pilihan == 1:
        print("Harga Untuk Anggota yang sudah lebih dari 5 bulan = 5000")
        print("Harga Untuk Anggota baru/ kurang dari 5 bulan = 2500")
    elif pilihan == 2:
        harga()  
  
