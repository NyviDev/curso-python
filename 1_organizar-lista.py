places=['Inglaterra','Grécia','Canadá','Espanha','França']
print('Lista Original:', places)
print('Lista temporária em ordem alfabética:', sorted(places))
print('Lista temporária em ordem alfabética inversa:', sorted(places,reverse=True))
places.reverse()
print('Lista inversa:', places)
places.reverse()
print('Lista original novamente:', places)
places.sort()
print('Lista em ordem alfabética:', places)
places.sort(reverse=True)
print('Lista em ordem alfabética inversa:', places)