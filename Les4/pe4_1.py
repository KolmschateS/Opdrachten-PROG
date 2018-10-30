aantalVakken = 3
cijferICOR = 6.5
cijferPROG = 8
cijferCSN = 7

cijfers = [cijferCSN + cijferICOR + cijferPROG]
gemiddelde = sum(cijfers) / aantalVakken
print(gemiddelde)

beloning = sum(cijfers) * 30
print(beloning)

print('Mijn gemiddelde, een: ', round(gemiddelde, 1), ' geeft mij een beloning van: ' , beloning, )
