'''
Taschenrechner-App
Version: 1.0
Creator: Laurence Piesold, Nerina Hauri
Beschreibung: Rechnet mit 2 Zahlen
'''
zahl1 = 0
zahl2 = 0
rechenoperation = ''
savedNumbers = []
taschenrechner = True
while taschenrechner:
    zahl1 = int(input('Geben Sie Ihre 1. Zahl ein: '))
    zahl2 = int(input('Geben Sie Ihre 2. Zahl ein: '))
    print(' 1) addieren \n 2) subtrahieren \n 3) multiplizieren \n 4) dividieren \n 5) gespeicherte Zahl verwenden')
    rechenoperation = input('Geben Sie Ihre Option ein: ')
    if rechenoperation == 1:
        produkt = zahl1 + zahl2

    elif rechenoperation == 2:
        produkt = zahl1 - zahl2

    elif rechenoperation == 3:
        produkt = zahl1 * zahl2

    elif rechenoperation == 4:
        produkt = zahl1 / zahl2

    else:
        print('Ungültige Operation')
        exit()

    print('Ihr Produkt ist:', produkt)

    wiederholung = input('Wollen Sie noch weiterrechnen j/n ?  ')
    wiederholung.lower()
    if wiederholung == 'n' or wiederholung == 'nein':
        taschenrechner = False

    if wiederholung == 'j' or wiederholung == 'ja':
        saveNumber = input('Benötigen Sie ihre Endzahl noch? j/n ?  ')
        saveNumber.lower()
        if saveNumber == 'j' or wiederholung == 'ja':
            savedNumbers.append(produkt)
            print(savedNumbers)