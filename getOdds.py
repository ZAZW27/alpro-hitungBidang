print('Program Mencetak Bilangan Ganjil N sampai 1')

N = int(input('Masukkan bilangan N : '))

while 1 <= N:
    if N % 2 != 0:
        print(N, end=' ')
    N -= 1
