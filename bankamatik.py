yusuf_hesap={
    'ad':'yusuf budak',
    'hesap_no':'12345678',
    'bakiye':3000,
    'ek_hesap':1000 
}
kadir_hesap={
    'ad':'kadir budak',
    'hesap_no':'12345600',
    'bakiye':4000,
    'ek_hesap':2000 
}
def para_cek(hesap,miktar):
    print(f"Merhaba,{hesap['ad']}")
    if (hesap['bakiye']>=miktar):
        print('Paranızı alabilirsiniz')
        hesap['bakiye'] -= miktar
        print(f"Hesap bakiyeniz:{hesap['bakiye']} ve ek bakiyeniz :{hesap['ek_hesap']}")

    else:
        toplam = hesap['bakiye'] + hesap['ek_hesap']
        if (toplam >= miktar):
            ek_hesap_kullanimi = input('ek hesap kullanılsın mı (e/h)')
            if ek_hesap_kullanimi=='e' or ek_hesap_kullanimi=='h':
                print('paranızı alabilirsiniz')
                hesap['ek_hesap'] -= miktar-hesap['bakiye']
                hesap['bakiye'] = 0
                print(f"Hesap bakiyeniz:{hesap['bakiye']} ve ek bakiyeniz :{hesap['ek_hesap']}")
            else :
                print(f"{hesap['hesap_no']} lu hesabınızda {hesap['bakiye']} TL  + {hesap['ek_hesap']} TL ek bakiye bulunmaktadır.")
        else :
            print('Üzgünüm bakiye yetmemektedir.')



para_cek(yusuf_hesap,1000)
para_cek(yusuf_hesap,1000)
para_cek(yusuf_hesap,1500)