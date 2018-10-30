import time

norm_p_km = 0.80  # Prijs per kilometer, normaal tarief, onder de 50 km
norm_p_max_d = 50  # Max aantal kilometer normaal tarief
p_50km_min = 10  # Minimale prijs boven 50 km tarief
p_50km = 0.60
min_age_disc = 65
max_age_disc = 12
dist = 50


def standard_p(d_km):
    if d_km < norm_p_max_d:
        p = norm_p_km * d_km
        return p
    else:
        d_km -= norm_p_max_d
        p = p_50km_min + (d_km * p_50km)
        return p


def ride_p(age, weekend, d_km):
    p = standard_p(d_km)
    if weekend:
        if min_age_disc >= age and age <= max_age_disc:
            p *= 0.65
            return p
        else:
            p *= 0.6
            return p
    else:
        if min_age_disc >= age and age <= max_age_disc:
            p *= 0.7
            return p
        else:
            return p


def inp_weekend():
    if input_weekend == 'Y':
        return True
    else:
        return False

print('Goededag, vul hier uw gegevens in voor uw tarief.')
time.sleep(0.5)
input_age = int(input("Uw leeftijd: "))
time.sleep(0.5)
input_weekend = input("Is het weekend? [Y/N] : ")
time.sleep(0.5)
input_dist = int(input("De afstand van uw reis.: "))
time.sleep(0.5)
print(f'Uw tarief is: {ride_p(input_age, inp_weekend(), input_dist)}')
time.sleep(1.5)
print('Fijne reis.')
