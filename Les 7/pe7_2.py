def kaartnummers(filename):
    infile = open(filename, 'r')
    data_list = infile.readlines()
    infile.close()
    return data_list

lst = kaartnummers('kaartnummers.txt')

for i in lst:
    i = i.strip()
    nummer, naam = i.split(',')

    print('{} heeft kaartnummer: {}'.format(naam, nummer), end='\n')

