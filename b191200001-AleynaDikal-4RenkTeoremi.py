"""
@author: Aleyna Dikal
@okulNo:B191200001
@OgretimGrup:1A
@ders:Ayrık Matematik
@konu:Dört Renk Teoremi
"""


komsulukMatrisi =   [[ 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                    [ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                    [ 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [ 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                    [ 1, 0, 0, 1, 0, 1, 0, 0 ,0, 0, 0],
                    [ 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [ 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                    [ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                    [ 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
                    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                    [ 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0]]


sehirlerListesi = ["Edirne","Kırklareli","İstanbul","Tekirdağ","Çanakkale","Balıkesir","Bursa","Yalova","Kocaeli","Sakarya","Bilecik"]

tutucuObje={}

for i in range(len(komsulukMatrisi)):
  tutucuObje[sehirlerListesi[i]] = i
  


derece =[]
for i in range(len(komsulukMatrisi)):
  derece.append(sum(komsulukMatrisi[i]))
renkObjesi= {}
for i in range(len(komsulukMatrisi)):
  renkObjesi[sehirlerListesi[i]]=["Kırmızı","Mavi","Yeşil","Sarı"]
  


siralanmisSehirler=[]
indeks = []
for i in range(len(derece)):
  maximum= 0
  for j in range(len(derece)):
    if j not in indeks:
      if derece[j] > maximum:
        maximum = derece[j]
        indeksTutucu = j
  indeks.append(indeksTutucu)
  siralanmisSehirler.append(sehirlerListesi[indeksTutucu])
  


sonuc={}
for sehirElemani in siralanmisSehirler:
  rengiAta = renkObjesi[sehirElemani]
  sonuc[sehirElemani] = rengiAta[0]
  komsuSehirler = komsulukMatrisi[tutucuObje[sehirElemani]]
  for j in range(len(komsuSehirler)):
    if komsuSehirler[j]==1 and (rengiAta[0] in renkObjesi[sehirlerListesi[j]]):
      renkObjesi[sehirlerListesi[j]].remove(rengiAta[0])
      
      
      

for sehirElemani,renkElemani in sorted(sonuc.items()):
  print("Şehir İsmi=",sehirElemani,"/ Şehir Rengi: ",renkElemani)
      

