# menggunakan list
panjang = int(input('masukkan panjangan deret:'))

fibo = [0, 1]

for i in range(2, panjang):
    print(f'deret ke {(i + 1)} \n')


for i in range(2, panjang):
    index1 = i - 2
    index2 = i - 1
    print(f'deret ke {(i + 1)} adalah index-{index1} + index-{index2} \n')


for i in range(2, panjang):
    angka1 = fibo[i - 2]
    angka2 = fibo[i - 1]
    angkaselajutnya = angka1 + angka2

    fibo.append(angkaselajutnya)

print(fibo)

# menggunakan variabel bantuan
panjang = int(input('masukkan panjang deret: '))

angka1, angka2 = 0, 1

for i in range(panjang):
    print(f'perulangan ke-{i} \n')

for i in range(panjang):
    if (i < 2):
        print(i, end='')
    else:
        angkasekarang = angka1 + angka2
        print(angkasekarang, end='')

        #update 2 variable bsntuan
        angka1 = angka2
        angka2 = angkasekarang