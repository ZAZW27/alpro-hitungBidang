import math
print ("Pilih bangun datar.")
invalid = "\033[31mInvalid input\033[37m"
while True:
    print ("1. Persegi panjang")
    print ("2. Persegi")
    print ("3. Segitiga")
    print ("4. Keluar")
    pilih_bidang = int(input("Masukkan angka bangun datar yang ingin anda cari...")) # mencari 
    
    if (pilih_bidang == 1):
        print ("1. Luas")
        print ("2. Keliling")
        jenis_hitungan = int(input("Pilih luas atau keliling...")) # menentukan mana yang akan dicari
        
        if jenis_hitungan != 1 and jenis_hitungan != 2: print(invalid ) ; continue

        panjang = int(input("Masukkan panjang...")) # cari panjang
        lebar = int(input("Masukkan lebar...")) # cari lebar
        if jenis_hitungan == 1 : # mencari luas
            luas = panjang * lebar
            print (f"Maka luas persegi panjang adalah {luas}")
        elif jenis_hitungan == 2 : # mencari keliling
            keliling = 2 * (panjang + lebar)
            print (f"Maka keliling persegi panjang adalah {keliling}")

    elif pilih_bidang == 2:
        print ("1. Luas")
        print ("2. Keliling")
        jenis_hitungan = int(input("pilih luas atau keliling...")) 
        
        if jenis_hitungan != 1 and jenis_hitungan != 2: print(invalid ) ; continue
        
        sisi = int(input("masukkan panjang sisi...")) # cari sisi awal 
        if jenis_hitungan == 1 :
            luas = sisi * sisi 
            print (f"maka luas persegi adalah {luas}")
        elif jenis_hitungan == 2 :
            keliling = 4 * sisi
            print (f"maka keliling persegi adalah {keliling}")

    elif pilih_bidang == 3 :
        print ("pilih jenis segitiga")
        print ("1. segitiga sama sisi")
        print ("2. segitiga pythagoras")
        print ("3. segitiga sama kaki")
        print ("4. segitiga sembarang")
        jenis_segitiga = int(input("pilih jenis segitiga..."))

        if jenis_segitiga == 1 : # sama sisi
            print ("1. luas")
            print ("2. keliling")
            jenis_hitungan = int(input("pilih luas atau keliling...")) # menentukan mana yang akan dicari
            
            if jenis_hitungan != 1 and jenis_hitungan != 2: print(invalid ) ; continue
            
            sisi = int(input("masukkan panjang sisi...")) # memberi sisi
            if jenis_hitungan == 1 : # mencari luas
                luas = math.sqrt(3) / 4 * (sisi)**2
                print (f"maka luas segitiga sama sisi adalah {luas}")
                
            elif jenis_hitungan == 2 : # mencari keliling
                keliling = 3 * (sisi)
                print (f"maka keliling segitiga sama sisi adalah {keliling}")

        elif jenis_segitiga == 2 : # pytagoras
            print ("sisi apa yang ingin kamu cari ?")
            print ("1. samping atau depan")
            print ("2. miring")
            jenis_hitungan = int(input("masukkan panjang sisi yang anda ingin cari..."))
            
            if jenis_hitungan == 1 :
                miring = int(input("masukkan panjang sisi miring..."))
                depan_samping = int(input("masukkan panjang sisi depan atau bawah yang diketahui..."))
                bawah_atas = math.sqrt((miring)**2 - (depan_samping)**2)
                print (f"maka panjang sisi yang kamu cari adalah {bawah_atas}")

            elif jenis_hitungan == 2 :
                depan = int(input("masukkan panjang sisi depan..."))
                samping = int(input("masukkan panjang sisi samping..."))
                miring = math.sqrt ((depan)**2 + (samping)**2)
                print (f"sisi miringnya adalah {miring}")

            else:
                print (invalid)
                
        elif jenis_segitiga == 3 : # sama kaki
            print ("1. luas")
            print ("2. keliling")
            jenis_hitungan = int(input("pilih luas atau keliling..."))
            
            if jenis_hitungan != 1 and jenis_hitungan != 2: print(invalid ) ; continue
            
            alas = int(input("masukkan panjang alas...")) # memberi alas awal
            if jenis_hitungan == 1 : # luas
                tinggi = int(input("masukkan tinggi..."))
                luas = 0.5 * alas * tinggi
                print (f"maka luas segitiga sama kaki adalah {luas}")
                
            elif jenis_hitungan == 2 : # keliling
                sisi = int(input("masukkaan panjang sisi..."))
                keliling = (2 * sisi) + alas
                print (f"maka keliling segitiga sama kaki adalah {keliling}")
                
        elif jenis_segitiga == 4 : # sembarang
            print ("1. keliling")
            print ("2. setengah keliling")
            print ("3. luas")
            jenis_hitungan = int(input("pilih luas atau keliling..."))
            
            if jenis_hitungan != 1 and jenis_hitungan != 2 and jenis_hitungan != 3: print(invalid ) ; continue
            
            a = int(input("masukkan panjang sisi a..."))
            b = int(input("masukkan panjang sisi b..."))
            c = int(input("masukkan panjang sisi c..."))
            
            if jenis_hitungan == 1 :
                keliling = a + b + c
                print (f"maka keliling segitiga sembarang adalah {keliling}")
                
            elif jenis_hitungan == 2 :
                setengah_keliling = (a + b + c) / 2
                print (f"jadi setengah keliling segitiga sembaranng adalah {setengah_keliling}")
                
            elif jenis_hitungan == 3 :
                setengah_keliling = int(input("masukkan setengah keliling segitiga sembarang..."))
                luas = math.sqrt(setengah_keliling * (setengah_keliling - a) * (setengah_keliling - b) * (setengah_keliling - c))
                print (f"maka luas segitiga sembarang adalah {luas}")
        else :
            print (invalid)
    elif pilih_bidang == 4 :
        print ("Sampai jumpa lagi!!!")
        break
    else:
        print (invalid)    