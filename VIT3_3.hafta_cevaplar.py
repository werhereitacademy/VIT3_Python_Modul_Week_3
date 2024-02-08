'''Proje Açıklaması: Bu ödevde, Python programlama dilini kullanarak bir görev yöneticisi uygulaması oluşturacaksınız. Bu uygulama, kullanıcılara görevlerini eklemelerine, tamamlamalarına, silmelerine ve listelemelerine olanak tanır.
'''


liste = []
bos_sira_numaralari = []
silinen_gorevler = []
def gorev_ekle(gorev,durum = 'Beklemede'):
    yeni_gorev = {'Görev': gorev , 'Durum' : durum, 'Sıra Numarası' : sira_numarasi_bul()}
    liste.append(yeni_gorev)
    return yeni_gorev
    
#sira numarasini listenin eleman sayisindan aliyoruz.

def sira_numarasi_bul():
    if len(bos_sira_numaralari) == 0:
        if len(liste) == 0:
            return 1
        else:
            return len(liste) + 1
     #bosta sira numarasi yoksa son elemanin sıra numarasinin bir fazlasini donduruyoruz.
     #eger bosta sira numarasi varsa en kucuk sira numrasini listeden cikarip donduruyoruz boylece ayni siraya sahip iki gorevi engelliyoruz.
    else:
        bos_sira_numaralari.sort()
        return bos_sira_numaralari.pop(0)
    
def gorevi_tamamla(sira_numarasi):
    for i in liste:
        if i['Sıra Numarası'] == sira_numarasi:
            i['Durum'] = 'Basarili'
            return i
        #eger gorev tamamlandi ise gorevi dondurecek aksi durumda False doner.
        #Dondurulen degeri kullanarak gorev tamamlanmasi kontrol edilir.
        #Boylece kullaniciya gerekli bilgi verilir.
    return False
        
def gorevi_sil(sira_numarasi):
    for gorev in liste:
        if gorev['Sıra Numarası'] == sira_numarasi:
            gorev['Durum'] = 'Silindi'
            silinen_gorevler.append(gorev)
            liste.remove(gorev)
            bos_sira_numaralari.append(sira_numarasi)
            return gorev
    return False
def tamamlanmis_gorevleri_listele():
    tamamlanmis_gorevler = []
    for gorev in liste:
        if gorev['Durum'] == 'Basarili':
            tamamlanmis_gorevler.append(gorev)
    return tamamlanmis_gorevler

def tum_gorevleri_listele():
    tum_liste = liste + silinen_gorevler
    tum_liste.sort(key = lambda i: i['Sıra Numarası'])
    return tum_liste
    return silinen_gorevler


def program():
    print('''
    1. Gorev Ekle
    2. Tamamla
    3. Gorev Sil
    4. Tamamlanmis Gorevleri Listele
    5. Tum Gorevleri Listele
    6. Cikis''')



    while True:
        secim = input('Yapmak istediginiz islemi seciniz: ')
        if secim == '1':
            gorev = input("GOREVI GIRINIZ:")
            yeni_gorev = gorev_ekle(gorev)
            print("Gorev Eklendi")
            print(yeni_gorev)
        
        elif secim == '2':
            sira_numarasi = int(input('Sıra Numarasını Giriniz: '))
            tamamlandi = gorevi_tamamla(sira_numarasi)
            if tamamlandi:
                print('Gorev Tamamlandı')
                print(tamamlandi)
            else:
                print('Gorev Bulunamadı')
        elif secim == '3':
            sira_numarasi = int(input('Sıra Numarasını Giriniz: '))
            silinen_gorev = gorevi_sil(sira_numarasi)
            if silinen_gorev:
                print('Gorev Silindi')
                print(silinen_gorev)
            else:
                print('Gorev Bulunamadı')
        
        elif secim == '4':
            print('Tamamlanmis Gorevler:')
            print(tamamlanmis_gorevleri_listele())
            
        elif secim == '5':
            print('Tum Gorevler:')
            print( tum_gorevleri_listele())
        
        elif secim == '6':
            print('Cikis Yapildi')
            break
        else:
            print('Hatali Secim')
                
program()            