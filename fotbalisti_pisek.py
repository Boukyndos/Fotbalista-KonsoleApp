import csv;
from pathlib import Path

path = Path('tjpisek_ml_zaci.csv')

if path.is_file() == False :
    hlavicka = ['Jmeno', 'Prijmeni', 'Cislo dresu', 'Pocet golu','Pozice']
    with open('tjpisek_ml_zaci.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(hlavicka)

pocet = int(input("Zadej počet hráčů které chceš přidat do týmu: ")); #Vytvořili jsme proměnnou pocet do které se pomocí input vkládá integer.

for i in range(pocet): # vytvorili jsme cyklus který se provede tolikrát jaký bude počet 
    jmeno = input("Zadej jméno hráče: ") # vytvorili jsme proměnu jmeno do ktere se zapise jmeno hrace string
    prijmeni = input("Zadej příjmení hráče: ") #vytvorili jsme proměnu jmeno do ktere se zapise prijmeni hrace string
    cislo = int(input("Zadej číslo dresu hráče" + " " + jmeno + " " + prijmeni + ": ")) # vytvorili jsme promennou cislo do ktere se pomociinput vkláda int
    goly = int(input("Kolik gólů nastřílel hráč" + " " + jmeno + " " + prijmeni + "? : ")) # vytvorili jsme promennou goly do ktere se pomoci input vkládá integer
    pozice = input("Zadej pozici hráče" + " " + jmeno + " " + prijmeni + ": ") 

    print("------------------------------------------------------")
    print("Hráč " + jmeno + " " + prijmeni + ", který hraje na pozici" + " " +pozice) # vypiš jméno a příjmení hráče, které jsou uloženy v proměnných jmeno a prijmeni
    print("Který má dres s číslem: " + str(cislo)) # vypiš jaké číslo má jeho dres pomocí metody str která převede int cislo na string
    print("Nastřílel " + str(goly) + " gólů." ) # vypiš kolik nastrilel golu pomocí metody str která převede int goly na string
    print("------------------------------------------------------")
    data = [jmeno, prijmeni, cislo, goly, pozice]

    with open('tjpisek_ml_zaci.csv', 'a+', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)