stundenlohn = input("Bitte gebe deinen Stundenlohn ein: ")
print("")
print("")
tag = 8 * int(stundenlohn)
woche = tag * 5
monat = tag * 20
jahr = monat * 12

print("Dein Stundenlohn beträgt: " + str(stundenlohn) + "€" )
print("Du verdienst " + str(tag) + "€ pro Tag")
print("Du verdienst " + str(woche) + "€ pro Woche")
print("Du verdienst " + str(monat) + "€ pro Monat")
print("Du verdienst " + str(jahr) + "€ pro Jahr")
print("")
print("")
input("Drücke eine beliebige Taste um das Programm zu schließen")
