def szybkie_sortowanie(tablica):
    if len(tablica)<2:
        return tablica
    else:
        pivot = tablica[0]
        less = [i for i in tablica[1:] if i<= pivot]
        greater = [i for i in tablica[1:] if i > pivot]

        return szybkie_sortowanie(less)+[pivot]+szybkie_sortowanie(greater)


do_posortowania=[1,3,2,9,8,5,4]
sortowanie = szybkie_sortowanie(do_posortowania)
print(sortowanie)