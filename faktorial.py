print ("Program Mencetak Perhitungan Faktorial")
n = int(input("Masukkan angka yang diinginkan untuk menghitung faktorial = "))
hasil_faktor = 1
penjumlahan_format = " "
angka = n

while True:
    hasil_faktor *= n
    penjumlahan_format += str(n)
    if n > 1:
        penjumlahan_format += " x "
    else: break
    n -= 1

print (f"Faktorial dari {angka} adalah {hasil_faktor} dengan format {angka}! = {penjumlahan_format}\n")