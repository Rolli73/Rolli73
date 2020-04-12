from operator import add, mul, sub, truediv


def eingabe():
    while True:
        try:
            a = int(input("1. Zahl: "))
            b = int(input("2. Zahl: "))
        except ValueError:
            print("Fehler: Zahl muss eine Ganzzahl sein!")
        else:
            return a, b


def rechenaufgabe_bearbeiten(rechenart, ergebnisbezeichnung, funktion):
    print(rechenart.upper())
    a, b = eingabe()
    ergebnis = funktion(a, b)
    print(
        f"\n{ergebnisbezeichnung.capitalize()}"
        f" von {a} und {b} ist {ergebnis}\n"
    )


def main():
    print("Taschenrechner 02.04.2020 By Roli\n")
    rechenarten = [
        "Addition",
        "Subtraktion",
        "Multiplikation",
        "Division",
    ]
    while True:
        for nummer, rechenoperation in enumerate(rechenarten):
            print(f"{nummer}. {rechenoperation}")
        print("0. EXIT")
        choice = int(input("Ihre Wahl? "))
        if choice == 0:
            print("\nAUF WIEDERSEHEN")
            break
        
        if choice == 1:
            rechenaufgabe_bearbeiten("Addition", "die Summe", add)
        elif choice == 2:
            rechenaufgabe_bearbeiten("Subtraktion", "die Differenz", sub)
        elif choice == 3:
            rechenaufgabe_bearbeiten("Multiplikation", "das Produkt", mul)
        elif choice == 4:
            rechenaufgabe_bearbeiten("Division", "der Quotient", truediv)
        else:
            print(
                f"Bitte nur Zahlen zwischen 0 und {len(rechenarten)} eingeben!"
            )


if __name__ == "__main__":
    main()