
# 0 dan büyük ve bir sayı olacak şekilde asker sayısını kullanıcıdan alan fonksyon
def askerSayısıAl():
    askerSayi=input("Toplam asker sayisini giriniz: ")
    if not askerSayi.isdigit():
        askerSayi=askerSayısıAl()
    elif int(askerSayi)<0:
         askerSayi=askerSayısıAl()     
    return int(askerSayi)

# 0 dan büyük ve bir sayı olacak şekilde mod sayısını kullanıcıdan alan fonksyon
def modSayısıAl():
    modSayi=input("İdamın kaçarlı adımla olacağını giriniz: ")
    if not modSayi.isdigit():
        modSayi=modSayısıAl()
    elif int(modSayi)<0:
         modSayi=modSayısıAl()     
    return int(modSayi)

# 1,2...asker sayisina kadar değerlerin olduğu listeyi oluşturan fonksiyon
def listeOlustur(boyut):
    liste=[]
    for i in range(boyut):
        liste.append(int(i+1))
    return liste


 


def idamlarıGerçekleştir(askerListesi,modSayisi):
    askersayisi = len(askerListesi)
    indis = 0
    askerinSıraNumarası = 1

    while askersayisi !=2:
        if indis >= len(askerListesi):# eğer dizinin sonuna gelirsek dizinin başından devam edelim diye indis=0 yapalım
            indis=0
        if askerListesi[indis]==0:
            indis+=1
        else:
            if askerinSıraNumarası % modSayisi ==0: # eğer askerin bulundugu sıra numarası mod sayısına tam bolunurse listenin o indisindeki eleman çıkarılır(0 yapılır)
               askerListesi[indis]=0
               askersayisi-=1
            indis += 1
            askerinSıraNumarası += 1
    return askerListesi







#Main
askerSayi = askerSayısıAl()
modSayi = modSayısıAl()
askerListesi = listeOlustur(askerSayi)
askerListesi = idamlarıGerçekleştir(askerListesi,modSayi)

for i in range (len(askerListesi)):
    if askerListesi[i]!=0:
        print(askerListesi[i],end=", ")
print()