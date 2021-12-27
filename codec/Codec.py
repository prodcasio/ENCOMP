import string
import unidecode

c = 0
parola = list(map(str, input("Inserisci delle parole: ").translate(str.maketrans('', '', string.punctuation)).rstrip(
    "\n").lower().split()))

for i in range(0, len(parola)):
    c = 0
    parola[i] = unidecode.unidecode(parola[i])
    with open("Italia2.txt") as file:
        for line in file:
            c = c + 1
            if line == parola[i] + "\n":
                if i != 0 and parola[i] == parola[i - 1]:
                    print(hex(0), "", end='')
                    break
                else:
                    print(hex(c).replace("0x", ""), "", end='')
                    break
            elif c == 279893 and parola[i].isnumeric() == False:
                print(parola[i], "", end='')
                break
            elif c == 279893 and parola[i].isnumeric() == True:
                parola[i] = hex(int(parola[i])).replace("0x", "") + '!'
                print(parola[i], "", end='')
                break

c = 0
temp = str("0")
numero = list(input("\nInserisci dei numeri: ").split())

for i in range(0, len(numero)):
    c = 0
    try:
        if ('!' in numero[i]) == True:
            numero[i] = int(numero[i], 16)
        else:
            numero[i] = int(numero[i], 16)
            numero[i] = str(numero[i])
    except:
        pass

    with open("Italia2.txt") as file:
        for line in file:
            c = c + 1
            if numero[i].isnumeric() == True and int(numero[i]) == 0:
                print(temp.strip(), "", end='')
                break
            elif numero[i].isnumeric() == True and c == int(numero[i]):
                print(line.strip(), "", end='')
                if i < len(numero) - 1:
                    if numero[i + 1] == 0:
                        temp = line
                break
            elif ('!' in numero[i]) == True:
                numero[i]=numero[i].replace("!", "")
                print(int(int(numero[i],16)), "", end='')
                break
            elif numero[i].isnumeric() == False:
                print(numero[i], "", end='')
                break