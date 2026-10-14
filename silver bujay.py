from datetime import datetime
while True:
    print("=== SISTEM PENGGAJIAN INGIN MAJU TERUS ===".center(78))


    tito= input("NAMA PEGAWAI\t:")
    titohadi= int(input("NIP \t\t:"))

    while True:
        try:
                titohadisatrio = int(input("TAHUN MASUK \t:"))        
                titohs= datetime.now().year
                titohadis= titohs - titohadisatrio
                if titohadis < 0:
                    print("Tahun masuk tidak boleh di masa depan. Silakan coba lagi.")
                    continue
                print(f"LAMA KERJA \t:{titohadis} tahun")
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan tahun dalam format angka.")  
    print(""" 
        PILIH JABATAN ANDA:
            1. Staff
            2. Manager
            3. Direktur
        """)
    ths = int(input("MASUKKAN PILIHAN JABATAN (1/2/3): "))
    if ths == 1:
            tithadsat = "Staff"
            tithsad =  2500000
            print(f"JABATAN ANDA \t:{tithadsat}")
            print(f"GAJI POKOK \t:Rp.{tithsad}")
    elif ths ==2:
            tithadsat = "Manager"
            tithsad =  3500000
            print(f"JABATAN ANDA \t:{tithadsat}")
            print(f"GAJI POKOK \t:Rp.{tithsad}")
    elif ths ==3:
            tithadsat = "Direktu
            tithsad =  7000000
            print(f"JABATAN ANDA \t:{tithadsat}")
            print(f"GAJI POKOK \t:Rp.{tithsad}")
    else:

            print("Pilihan jabatan tidak valid.")

    print(""" 
        STATUS PEGAWAI:
            1. TETAP 
            2. HONORER
        """)
    satriotitohadi = int(input("MASUKKAN PILIHAN STATUS PEGAWAI (1/2): "))
    if satriotitohadi == 1:
            satriotitohadii = "TETAP"
            hadisatriotito = 2*tithsad
            titoo= 10000
            print(f"STATUS PEGAWAI \t\t:{satriotitohadii}")
            print(f"TUNJANGAN \t\t:Rp{hadisatriotito}")
            print(f"TUNJANGAN TRANSPORT \t:Rp{titoo}")
    elif satriotitohadi == 2:
            satriotitohadii = "HONORER"
            hadisatriotito = 0
            titoo= 25*15000
            print(f"STATUS PEGAWAI \t\t:{satriotitohadii}")
            print(f"TUNJANGAN \t\t:Rp{hadisatriotito}")
            print(f"TUNJANGAN TRANSPORT \t:Rp{titoo}")
    else:
            print("Pilihan status pegawai tidak valid.")

    print("""
        PILIH STASUS MENIKAH :
            1. MENIKAH
            2. BELUM MENIKAH
        """)
    hadiii = int(input("MASUKKAN PILIHAN STATUS MENIKAH (1/2): "))
    if hadiii == 1:
            hadiii_satrio ="MENIKAH"
            hadisatriooo = 250000
            titooohadi = int(input("JUMLAH ANAK :"))
            satrioooo= min(titooohadi,3)
            tithads = 200000 * satrioooo
            print(f"STATUS MENIKAH \t:{hadiii_satrio}")
            print(f"TUNJANGAN ISTRI t:Rp{hadisatriooo}")
            print(f"tunjangan anak \t:Rp{tithads}")
    elif hadiii == 2:
            hadiii_satrio ="BELUM MENIKAH"
            hadisatriooo = 0
            satrioooo= min(0,3)
            tithads = 0
            print(f"STATUS MENIKAH \t:{hadiii_satrio}")
            print(f"TUNJANGAN ISTRI :Rp{hadisatriooo}")
            print(f"tunjangan anak \t:Rp{tithads}")
    else:
            print("Pilihan status menikah tidak valid.")
    print("="*78)
    print(f"proses gaji karyawan: {tito}")
    print(f"GAJI POKOK :{tithsad}")
    if satriotitohadi == 1:
            print(f"TUNJANGAN :Rp{hadisatriotito}")
            print(f"TUNJANGAN TRANSPORT :Rp{titoo}")
    if satriotitohadi == 2:
            print(f"TUNJANGAN :Rp{hadisatriotito}")
            print(f"TUNJANGAN TRANSPORT :Rp{titoo}")
    if hadiii == 1:
            print(f"TUNJANGAN ISTRI :Rp{hadisatriooo}")
            print(f"TUNJANGAN ANAK :Rp{tithads}")
    print("="*78)
    titohadisatriooo= tithsad + hadisatriotito + titoo + hadisatriooo +tithads
    print(f"TOTAL GAJI ANDA :Rp{titohadisatriooo}")
    satriohadititooo= 0.10*tithsad
    print(f"PPH :Rp{satriohadititooo}")
    tihasa= titohadisatriooo - satriohadititooo
    print(f"GAJI BERSIH ANDA :Rp{tihasa}")
    print("="*78)
    print("\nPROGRAMER:")
    tito_hadi = int(input("NIM \t:"))
    if tito_hadi == "":
                print("NIM tidak boleh kosong!")
    else:
            print("NAMA \t:TITO HADI SATRIO")

    try:
                tito_hadi_satrio = input("Apakah Anda Ingin Mengulang menggunakan program ini? (Y/T): ").upper()
                if tito_hadi_satrio == "Y":
                    print("Silakan jalankan ulang program untuk menggunakan kembali.")
                    continue 
                else:
                    print("\nTerima kasih telah menggunakan program ini 🙏")
                break 
    except ValueError:
                print("Input tidak valid. Silakan masukkan Y atau T.")