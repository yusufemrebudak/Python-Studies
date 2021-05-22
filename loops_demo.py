
sayi = int(input('Sayi giriniz: '))
i=2
asal_mi=True
while i < sayi:
    if(sayi%i==0):
        asal_mi=False
        break
    i+=1
if asal_mi:
    print(f'{sayi} asaldır.')
else:
    print(f'{sayi} asal degildir.')