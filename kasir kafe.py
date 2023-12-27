import datetime

pilihan="y"
while pilihan=="y":
    print("""
              Cafe Bren
    ==============================
    List Menu
    A. ES Kopi Susu     : Rp 6.000
    B. ES Kopi Coklat   : Rp 8.000
    C. Mi Rebus         : Rp 7.000
    D. Ice Americano    : Rp 9.000
    E. ES Cincau        : Rp 5.000
    F. Mie Goreng       : Rp 7.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "a":
        listnama= "ES Kopi Susu"
        harga=(6000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "b":
        listnama= "ES Kopi Coklat"
        harga = (8000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "c":
        listnama= "Mi Rebus"
        harga=int(7000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "d":
        listnama= "Ice Americano"
        harga=int(9000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "e":
        listnama= "ES Cincau"
        harga=int(5000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    elif pesan == "f":
        listnama= "Mi Goreng"
        harga=int(7000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")

    print("--------------------------")
    print("        Cafe Bren")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    Tunai=int(input("Masukkan Pembayaran: "))
    hu=totalharga-Tunai
    kembali=Tunai-totalharga
    if(Tunai>totalharga):
        print("Kembali Rp.", kembali)
    else:
        print("Hutang Rp.", hu)
    pilihan=input("apakah anda ingin order kembali Y/N =")
