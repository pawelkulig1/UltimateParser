#'''
#from bs4 import BeautifulSoup
import requests
import re

input_arr = ["666039017"]

req = requests.get("http://allegro.pl/samsung-galaxy-s2-i9100-bialy-wysylka-z-polski-i7014133170.html")

data = str(req.text)

p = re.compile("\d\d\d\s*\d\d\d\s*\d\d\d")
m = p.findall(data)

delArr = []
for i in range(len(m)):
    if m.count(m[i])>2:
        delArr.append(i)

for i in range(len(delArr)-1, -1, -1):
    m.pop(delArr[i])

refPoz = 0
refArr = ["tel:", "seller-contact-data", "kontakt"]
refPozArr = []
for el in refArr:
    for i in range(100):
        refPoz = data.find(el, refPoz+1)
        if refPoz == -1:
            break
        refPozArr.append(refPoz)

elPozArr = []
for poz, el in enumerate(m):
    if(poz == 0):
        elPozArr.append(data.find(el))
    else:
        elPozArr.append(data.find(el, elPozArr[poz-1]))

refPozArr = list(set(refPozArr))
elPozArr.sort()
refPozArr.sort()

print(elPozArr, refPozArr)

wynik = [0, abs(elPozArr[0]-refPozArr[0])]
for poz, j in enumerate(elPozArr):
    suma = 0
    for i in refPozArr:
        suma = suma + abs(i-j)
        if(suma<wynik[1]):
            wynik = [poz, suma]

print(m[wynik[0]])
