print ("Program Mencetak Perhitungan Faktorial")
n = int(input("Masukkan angka yang diinginkan untuk menghitung faktorial = "))
Faktorial = 1
angka = n
hasil = " "

while True:
    Faktorial *= angka
    hasil += str(angka)
    if angka > 1:
        hasil += " x "
    else: break
    angka -= 1

print (f"Faktorial dari {n} adalah {Faktorial} dengan format {n}! = {hasil}")