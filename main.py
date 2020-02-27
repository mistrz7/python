#deklaracja funkcji
def pokaz_tekst(tekst):
    print("dostalem do wydruku->"+tekst)

def sumuj(tablica):
    total = 0;
    for x in tablica:
        total+=x
    return total


#cos sobie wydrukuj
print("start")


#test kondiszjonala
x=1
if x==1:
    pokaz_tekst("x=1")

#plik se otworze
f=open("//app/wildfly-18.0.0.Final/standalone/log/server.log", "r")
print(f.read(5))
print(f.readline())

for x in f:
    print(x)

f.close()

#print sumuj([1,2,3,4,5,6,7,8,9,0,11,12,13,14,15])


print("stop")
