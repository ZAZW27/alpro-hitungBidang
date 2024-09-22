faktor = int(input("Masukkan nilia untuk difaktorkan: "))
hasil = 1

while faktor != 0: 
    hasil *= faktor
    faktor -= 1

print(hasil)