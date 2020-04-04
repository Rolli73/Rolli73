import sys
import sys

def adition(wert1,wert2):
    ergebnis = wert1+wert2
    return ergebnis

def subtraktion(wert1,wert2):
    ergebnis = wert1-wert2
    return ergebnis

def multiplikation(wert1,wert2):
    ergebnis = wert1*wert2
    return ergebnis

def division(wert1,wert2):
    ergebnis = wert1/wert2
    return ergebnis

def eingabe():
       global a,b
       while True:
           try:
              a = int(input("1. Zahl : "))
              b = int(input("2. Zahl : "))
           except ValueError:
               print("Fehler: Zahl muss eine Ganzzahl sein!!")
           else:
                break
        
print("Taschenrechner 02.04.2020 By Roli\n")

while True:
    print(
        "1. Addition",
        "2. Subtraktion",
        "3. Multiplikation",
        "4. Division",
        "5. EXIT",
        "",
        sep="\n"
    )
    choise = int(input("Ihre Wahl? "))
    if choise == 1:
        print("ADDITION")
        eingabe()
        print("\nDie Summe von ",a," und ",b," = ",adition(a,b))
        print()
 
    elif choise == 2:
        print("SUBTRAKTION")
        eingabe()
        print("\nDie Differenz von ",a," und ",b," = ",subtraktion(a,b))
        print()

    elif choise == 3:
        print("MULTIPLIKATION")
        eingabe()
        print("\nDas Produkt von ",a," und ",b," = ",multiplikation(a,b))
        print()
 
    elif choise == 4:
        print("DIVISION")
        eingabe()
        print("\nDer Quotient von ",a," und ",b," = ",division(a,b))
        print()

    elif choise ==5:
        print("\nAUF WIEDERSEHEN")
        sys.exit()

    else:
        print("Bitte nur Zahlen zwischen {} und {} eingeben!".format(1,5))
        
        

