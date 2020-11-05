import json
from datetime import datetime, timedelta


def erfasste_zeit_laden(): # Die .json Datei wird geöffnet (read) oder neu erstellt.
    try:
        with open("zeiterfassung.json", "r") as open_file:  # Wenn die Datei "zeiterfassung.json" vorhanden ist, wird sie geöffnet.
            zeiterfassung = json.load(open_file)  # json.load wandelt den Text in der JSON-Struktur in Python-Dictionarys bzw. Listen um.
    except FileNotFoundError:
        zeiterfassung = {}  # Wenn noch keine Datei "zeiterfassung.json" vorhanden ist, wird ein leeres Dict erstellt.
    except json.decoder.JSONDecodeError:
        print("Die Datei scheint leer oder ungültig zu sein.")
        zeiterfassung = {}
    return zeiterfassung


def zeiterfassung_abspeichern(zeiterfassung): # Die Daten werden neu abgespeichert.
    with open("zeiterfassung.json", "w") as open_file:  # "zeiterfassung.json" wird im Schreibmodus geöffnet.
        json.dump(zeiterfassung, open_file)  # json.dump() wandelt Python-Dictionarys bzw. Listen in Text in der JSON-Struktur um.


def neue_eingabe_speichern(datum, aufgabe, startzeit, endzeit, pause):
    zeiterfassung = erfasste_zeit_laden()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    datum = datum + ", " + current_time

    startzeit_obj = datetime.strptime(startzeit, '%H:%M')
    endzeit_obj = datetime.strptime(endzeit, '%H:%M')
    pause = timedelta(minutes=int(pause))

    gesamtzeit = endzeit_obj - startzeit_obj - pause
    gesamtzeit = str(gesamtzeit)

    zeiterfassung[datum] = aufgabe, gesamtzeit

    zeiterfassung_abspeichern(zeiterfassung)