Januari = 1
Februari = 2
March = 3
April = 4
May = 5
June = 6
July = 7
August = 8
September = 9
Oktober = 10
November = 11
December = 12

def season(month):
    if month == 12 or month <= 2:
        print('Het is winter.')
    elif 3 <= month <= 5:
        print('Het is lente.')
    elif 6 <= month <= 8:
        print('Het is zomer.')
    else:
        print('Het is herfst.')

print(season(input('Welke maand is het?: ')))