auswahl = float(input("Auswahlmöglichkeiten: 1 Pfannkuchen 2 Waffeln 3 Käsekuchen (1 / 2 / 3): "))

if auswahl == 1:
    portions = float(input("Anzahl der Portionen für Pfannkuchen: "))

    for x in [str(portions * 1) + " Ei(er)", str(portions * 75) + "g Mehl", str(portions * 100) + "ml Milch"]:
        print("")
        print (x)




if auswahl == 2:
    portions = float(input("Anzahl der Portionen für Waffeln: "))

    for x in [str(portions * 0.5) + " Ei(er)", str(portions * 75) + "g Mehl", str(portions * 50) + "ml Milch" , str(portions * 50) + "g Butter" , str(portions * 50) + "g Zucker"]:
        print("")
        print (x)




if auswahl == 3:
    portions = float(input("Anzahl der Portionen für Käsekuchen: "))

    for x in [str(portions * 1) + " Ei(er)", str(portions * 10) + "g Mehl", str(portions * 20) + "ml Milch" , str(portions * 10) + "g Butter" , str(portions * 20) + "g Zucker" , str(portions * 80) + "g Quark"]:
        print("")
        print (x)
print("")
print("")
input("Beliebige Taste drücken um das Programm zu beenden...")
