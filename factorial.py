print ("Program Mencetak Perhitungan Faktorial")
n = int(input("Masukkan angka yang diinginkan untuk menghitung faktorial = "))
Faktorial = 1
angka = n
hasil = " "
i = 1

while i <= n:
    Faktorial *= i
    hasil += str(angka)
    if angka > 1:
        hasil += " x "
    i += 1
    angka -= 1

print (f"Faktorial dari {n} adalah {Faktorial} dengan format {n}! = {hasil}")